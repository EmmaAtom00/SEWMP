from flask import render_template, redirect, url_for, flash
from packages.form import RegistrationForm, LoginForm
from packages import app

@app.route("/")
def homepage():
    return render_template("index.html", title = "Home")

@app.route("/register")                     
def register():
    form = RegistrationForm()
    return render_template("register.html", form = form, title = "Registration")

@app.route("/login", methods = ["GET", "POST"])
def loginpage():
    form = LoginForm()
    return render_template("login.html", form =form, title = "Login")


@app.route("/about")
def about():
    return render_template("about.html", title = "About")
