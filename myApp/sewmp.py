from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index.html", title = "Home")

@app.route("/register")
def register():
    return render_template("register.html", title = "Registration")

@app.route("/login")
def loginpage():
    return render_template("login.html", title = "Login")

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

if (__name__) == "__main__":
    app.run(debug = True)
