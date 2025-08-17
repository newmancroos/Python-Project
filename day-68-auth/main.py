from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create table in DB with the UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

# with app.app_context():
#     db.create_all()

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Configure a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":

        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        userdata = result.scalar()

        if userdata:
            flash("You've already signed up with this email, login instead!")
            return redirect(url_for('login'))

        user = User(
            email=request.form.get("email"),
            password = generate_password_hash(request.form.get("password"),method='pbkdf2:sha256', salt_length=8),  #scrypt, https://flask-login.readthedocs.io/en/latest/
            name= request.form.get("name")
        )
        db.session.add(user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(user)
        return render_template("secrets.html", name=request.form.get("name"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email entered.
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if not user:
            flash("Email does not exist!")
            return redirect(url_for('login'))
        # Check stored password hash against entered password hashed.
        elif not check_password_hash(user.password, password):
            flash("Username or Password incorrect!")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", logged_in=current_user.is_authenticated)


@app.route('/download')
@login_required
def download():
    return send_from_directory("static","files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
