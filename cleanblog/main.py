from flask import Flask, render_template
import requests
app =Flask(__name__)


blog_url="https://api.npoint.io/b5cbefb545757e087e70"

response = requests.get(blog_url)
response_json = response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=response_json)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in response_json:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__=="__main__":
    app.run(debug=True)