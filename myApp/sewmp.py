from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Hello, World</h1>"

@app.route("/login")
def loginpage():
    return render_template("login.html", title = "Login")

if (__name__) == "__main__":
    app.run(debug = True)
