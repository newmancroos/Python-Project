from flask import Flask, render_template  #jinja already bundled with Flask
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    cyear = datetime.now().year
    return render_template("index.html", random_number=random_number, cyear=cyear)

@app.route('/guess/<name>')
def guessage(name):
    genderize_url="https://api.genderize.io"
    agify_url="https://api.agify.io"
    params ={"name": name}
    response_gender = requests.get(genderize_url, params=params)
    gender = response_gender.json()["gender"]
    response_age=requests.get(agify_url, params=params)
    age=response_age.json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def blog():
   blog_post_url = "https://api.npoint.io/0e8f03ddef34d6db0fdd"
   response = requests.get(blog_post_url)
   all_posts=response.json()
   return render_template("blog.html",posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


