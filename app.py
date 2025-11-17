from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    ...


@app.route("/create_account")
def create_account():
    ...


@app.route("/following")
def following():
    ...


@app.route("/profile")
def profile():
    ...


if __name__ == "__main__":
    app.run(debug=True)