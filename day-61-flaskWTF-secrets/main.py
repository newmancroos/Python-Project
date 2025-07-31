from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt
pip install email_validator

This will install the packages from requirements.txt for this project.
'''
# python - m pip install - r requirements.txt
# pip install bootstrap-flask

app = Flask(__name__)


app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)

class Login(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email("Valid Email")])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form = Login()
    if form.validate_on_submit() == True:  #Post return
        if form.email.data == "admin@email.com" and  form.password.data == "12345678" :
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form, bootstrap=bootstrap)



if __name__ == '__main__':
    app.run(debug=True)
