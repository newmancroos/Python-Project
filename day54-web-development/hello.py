from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    return "Hello world!"
@app.route("/bye")

# @make_bold
# @make_emphasis
# @make_underlined
def say_bye():
    return "<h1 style='text-align:center'>Bye</h1>"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/greetpath/<path:name>")   #This will return all the url part after greet poit
def greetpath(name):
    return f"Hello {name}"

@app.route("/multiparams/<name>/<int:number>")   #This will return all the url part after greet poit
def multiparams(name, number):
    return f"Hello {name}, {number}"

if __name__ == "__main__":
    app.run(debug=True) #If Debug = True then we can change anything and save will reload the page and will show the updated change without stop and start the website