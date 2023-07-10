from flask import render_template, redirect, url_for, flash
from packages.form import RegistrationForm, LoginForm
from packages import app, db, bcrypt
from packages.models import user, create_task
from flask_login import login_user, current_user, logout_user

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html", title = "Home")

@app.route("/register", methods =["GET", "POST"])                     
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()

    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        User = user(username = username, email = email, firstname = firstname, lastname = lastname, password = password)
        db.session.add(User)
        db.session.commit()

        flash(f"Registration successful {form.firstname.data}! you can proceed to login", "success")
        return redirect(url_for("loginpage"))
    return render_template("register.html", form = form, title = "Registration")

@app.route("/login", methods = ["GET", "POST"])
def loginpage():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        remember = form.remember_me.data

        User = user.query.filter_by(email=form.email.data).first()
        if User and bcrypt.check_password_hash(User.password, password):
            login_user(User, remember)
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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))