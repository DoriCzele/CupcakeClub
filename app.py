import os
from flask import Flask, render_template, request, url_for, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DB")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
pymongo = PyMongo(app)


@app.route("/base")
def temp_base_test():
    return render_template("layout/base.html")


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "pages/error.html", status_code=404, error_prompt="Are you lost?"
        ),
        404,
    )


@app.errorhandler(403)
def page_not_authorized(error):
    return (
        render_template(
            "pages/error.html",
            status_code=403,
            error_prompt="You cannot access this page.",
        ),
        403,
    )


@app.errorhandler(500)
def page_server_error(error):
    return (
        render_template(
            "pages/error.html",
            status_code=500,
            error_prompt="There has been an error somewhere!",
        ),
        500,
    )


@app.route("/")
def home():
    return render_template("pages/home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("A form has been submitted")
        pass
    # "http://localhost:8000/login"
    return render_template(
        "pages/authentication.html",
        auth_mode="Login",
        current_auth_link=url_for("login"),
        alternative_auth_mode="Register",
        alternative_auth_prompt="Create an account",
        alternative_auth_link=url_for("register"),
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if both provided
        try:
            username = request.form.get("username").lower()
            password = request.form.get("password")
            if username != "" and password != "":
                hashed_password = generate_password_hash(password)
                user = {"username": username, "password": hashed_password}
                username_already_exists = pymongo.db.users.find_one(
                    {"username": username}
                )
                if not username_already_exists:
                    pymongo.db.users.insert_one(user)
                    # redirect to homepage
                    # return redirect(url_for("home"))
                else:
                    flash("That username is taken, please try another.")
        except Exception as exception:
            flash("There has been an error, please try again later.")
    return render_template(
        "pages/authentication.html",
        auth_mode="Register",
        current_auth_link=url_for("register"),
        alternative_auth_mode="Login",
        alternative_auth_prompt="Already a member?",
        alternative_auth_link=url_for("login"),
    )


@app.route("/new-recipe")
def new_recipe():
    return render_template("pages/newrecipe.html")


if __name__ == "__main__":
    app.run(host="localhost", port="8000", debug=True)
