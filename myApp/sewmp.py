from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm


app = Flask(__name__)
app.config[ 'SECRET_KEY' ] = '0x7e7'

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html", title = "Home")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", form = form, title = "Registration")

@app.route("/login", methods = ["GET", "POST"])
def loginpage():
    form = LoginForm()
    return render_template("login.html", form = form, title = "Login")

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

if (__name__) == "__main__":
    app.run(debug = True)
