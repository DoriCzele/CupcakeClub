import os
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DB")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
pymongo = PyMongo(app)


GENERIC_ERROR_MESSAGE = "There has been an error, please try again later."
ALREADY_AUTHED_MESSAGE = "You are logged in!"


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
            error_prompt=GENERIC_ERROR_MESSAGE,
        ),
        500,
    )


@app.route("/")
def home():
    return render_template("pages/home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if bool("user" in session):
        flash(ALREADY_AUTHED_MESSAGE)
        return redirect(url_for("home"))
    if request.method == "POST":
        try:
            username = request.form.get("username").lower()
            password = request.form.get("password")
            db_user = pymongo.db.users.find_one({"username": username})
            if db_user is None:
                flash("This user does not exist. Please check your details and try again.")
                return redirect(url_for("login"))
            if check_password_hash(db_user["password"], password):
                session["user"] = str(db_user["_id"])
                flash(f"Welcome back {username}!")
                return redirect(url_for("home"))
            flash("Incorrect credentials. Please check your details and try again.")
        except Exception as exception:
            flash(GENERIC_ERROR_MESSAGE)
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
    if bool("user" in session):
        flash(ALREADY_AUTHED_MESSAGE)
        return redirect(url_for("home"))
    if request.method == "POST":
        # check if both provided
        try:
            username = request.form.get("username").lower()
            password = request.form.get("password")
            if username != "" and password != "":
                hashed_password = generate_password_hash(password)
                user = {"username": username, "password": hashed_password, "is_admin":False}
                username_already_exists = pymongo.db.users.find_one(
                    {"username": username}
                )
                if not username_already_exists:
                    pymongo.db.users.insert_one(user)
                    flash("Welcome to The Cupcake Club!")
                    return redirect(url_for("home"))
                else:
                    flash("That username is taken, please try another.")
        except Exception as exception:
            flash(GENERIC_ERROR_MESSAGE)
    return render_template(
        "pages/authentication.html",
        auth_mode="Register",
        current_auth_link=url_for("register"),
        alternative_auth_mode="Login",
        alternative_auth_prompt="Already a member?",
        alternative_auth_link=url_for("login"),
    )


@app.route("/logout")
def logout():
    if bool("user" in session):
        del session["user"]
    return redirect(url_for('home'))


@app.route("/create-recipe", methods=["GET", "POST"])
def new_recipe():
    if not bool("user" in session):
        return redirect(url_for("login"))
    if request.method == "POST":
        try:
            recipe_name = request.form.get("name").lower()
            ingredients = []
            instructions = []
            for key, value in request.form.items():
                if key.startswith("ingredient"):
                    ingredients.append(value.lower())
                if key.startswith("instruction"):
                    instructions.append(value.lower())
            color = request.form.get("radio").replace("#","")

            recipe = {
                "name": recipe_name,
                "ingredients": ingredients,
                "instructions": instructions,
                "color": color,
                "author": session["user"]
            }
            pymongo.db.recipes.insert_one(recipe)
            # After successful create recipe, redirect to recipe detail
        except Exception as exception:
            flash(GENERIC_ERROR_MESSAGE)
    return render_template("pages/edit-recipe.html")

@app.route("/recipes")
def recipes():
    recipes = pymongo.db.recipes.find()
    return render_template("layout/recipes.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("HOST"), port=os.environ.get("PORT"), debug=os.environ.get("DEBUG"))
