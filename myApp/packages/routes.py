from flask import render_template, redirect, url_for, flash
from packages.form import RegistrationForm, LoginForm
from packages import app
from packages.models import user, create_task

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
    if form.validate_on_submit():
        if form.email.data == admin@swemp.com and form.password.data == 'password':
            flash("Login Successful", 'success')
            return redirect(url_for('homepage'))
        else:
            flash("Username or Password incorrect")

    return render_template("login.html", form =form, title = "Login")


@app.route("/about")
def about():
    return render_template("about.html", title = "About")
