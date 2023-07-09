from flask import render_template, redirect, url_for, flash
from packages.form import RegistrationForm, LoginForm
from packages import app, db, bcrypt
from packages.models import user, create_task

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html", title = "Home")

@app.route("/register", methods =["GET", "POST"])                     
def register():
    form = RegistrationForm()
    email = form.email.data
    if form.validate_on_submit():
        flash(f"Registration successful {form.username.data}! you can proceed to login", "success")
        return redirect(url_for("loginpage"))
    return render_template("register.html", form = form, title = "Registration")

@app.route("/login", methods = ["GET", "POST"])
def loginpage():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        if email == "admin@swemp.com" and password == 'password':
            flash(f"Login Successful", 'success')
            return redirect(url_for('dashboard'))
        else:
            flash(f"Username or Password incorrect", 'danger')

    return render_template("login.html", form =form, title = "Login")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/about")
def about():
    return render_template("about.html", title = "About")
