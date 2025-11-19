from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    ...


@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]


        
    return render_template("create_account.html")


@app.route("/post")
def post():
    ...


@app.route("/following")
def following():
    ...


@app.route("/profile")
def profile():
    ...


if __name__ == "__main__":
    app.run(debug=True)