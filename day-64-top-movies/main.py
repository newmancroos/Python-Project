from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 
On Windows type:
python -m pip install -r requirements.txt

'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

# CREATE DB
db= SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    title:Mapped[str]= mapped_column(String(200), unique=True, nullable=False)
    year:Mapped[int] = mapped_column(Integer, nullable=False)
    description:Mapped[str]=mapped_column(String(200))
    rating:Mapped[float]=mapped_column(Float)
    ranking:Mapped[int]=mapped_column(Integer)
    review:Mapped[str]= mapped_column(String(250))
    img_url:Mapped[str]=mapped_column(String(200))
    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'

class RateMovieForm(FlaskForm):
    rating= StringField("Your Rating Out od 10 e.g. 7.5")
    review = StringField("Your Review")
    Submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


MOVIE_DB_API_KEY="b577a50e45b1bc035b5bc3bb26631ef2"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
# with app.app_context():
#     db.create_all()

# new_movie=Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

@app.route("/")
def home():
    all_movies = db.session.scalars(db.select(Movie).order_by(Movie.rating)).all()
    return render_template("index.html", allmovies=all_movies)

@app.route("/edit", methods=['GET','POST'])
def rate_movie():
    movie_id=request.args.get("id")
    movie = db.get_or_404(Movie,movie_id)
    form=RateMovieForm()

    if form.validate_on_submit():
        movie.rating=float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete")
def delete_movie():
    movie_id=request.args.get("id")
    movie = db.get_or_404(Movie,movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET","POST"])
def add_movie():
    MOVIE_DB_SEARCH_URL="https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        print(data)
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            rating=0,
            ranking=10,
            review="none",
            img_url=f"{MOVIE_DB_IMAGE_URL}/{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))

    return render_template("select.html")

if __name__ == '__main__':
    app.run(debug=True)
