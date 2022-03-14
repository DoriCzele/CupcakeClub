import os
from datetime import datetime
import re
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DB")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
pymongo = PyMongo(app)


GENERIC_ERROR_MESSAGE = "There has been an error, please try again later."
ALPHANUMERICAL_AND_SPACES_REGEX_STRING = "[A-Za-z0-9 ]+"
INPUT_FORMAT_ERROR_MESSAGE = "The provided values did not fulfil the format requirements."
ALREADY_AUTHED_MESSAGE = "You are logged in!"
DEFAULT_RECIPE_COLOR = "E8C0D9"


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

def regex_pattern_check(regex_pattern, string_to_evaluate):
    if regex_pattern.fullmatch(string_to_evaluate):
        return True
    raise ValueError(INPUT_FORMAT_ERROR_MESSAGE)

@app.route("/")
def home():
    return render_template("pages/home.html")

def get_auth_url_params(request, current_auth_link, alternative_auth_link):
    next_endpoint = None
    if request.args.get("next"):
        next_endpoint = request.args.get("next")
        current_auth_link = f"{current_auth_link}?next={next_endpoint}"
        alternative_auth_link = f"{alternative_auth_link}?next={next_endpoint}"
    return [next_endpoint, current_auth_link, alternative_auth_link]

@app.route("/login", methods=["GET", "POST"])
def login():
    current_auth_link = url_for("login")
    alternative_auth_link = url_for("register")
    next_endpoint = None
    next_endpoint, current_auth_link, alternative_auth_link = get_auth_url_params(request, current_auth_link, alternative_auth_link)
    if bool("user" in session):
        flash(ALREADY_AUTHED_MESSAGE)
        return redirect(url_for("home"))
    if request.method == "POST":
        try:
            regex_pattern = re.compile(ALPHANUMERICAL_AND_SPACES_REGEX_STRING)
            username = request.form.get("username").lower()
            if regex_pattern_check(regex_pattern, username):
                if len(username) < 5 or len(username) > 50:
                    raise ValueError
            password = request.form.get("password")
            db_user = pymongo.db.users.find_one({"username": username})
            username_title = username.title()
            if db_user is None:
                flash("This user does not exist. Please check your details and try again.")
                return redirect(current_auth_link)
            if check_password_hash(db_user["password"], password):
                session["user"] = str(db_user["_id"])
                flash(f"Welcome back {username_title}!")
                if next_endpoint:
                    return redirect(url_for(next_endpoint))
                return redirect(url_for("home"))
            flash("Incorrect credentials. Please check your details and try again.")
        except Exception:
            flash(GENERIC_ERROR_MESSAGE)
    return render_template(
        "pages/authentication.html",
        auth_mode="Login",
        current_auth_link=current_auth_link,
        alternative_auth_mode="Register",
        alternative_auth_prompt="Create an account! ",
        alternative_auth_link=alternative_auth_link,
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    current_auth_link = url_for("register")
    alternative_auth_link = url_for("login")
    next_endpoint = None
    next_endpoint, current_auth_link, alternative_auth_link = get_auth_url_params(request, current_auth_link, alternative_auth_link)
    if bool("user" in session):
        flash(ALREADY_AUTHED_MESSAGE)
        return redirect(url_for("home"))
    if request.method == "POST":
        # check if both provided
        try:
            regex_pattern = re.compile(ALPHANUMERICAL_AND_SPACES_REGEX_STRING)
            username = request.form.get("username").lower()
            if regex_pattern_check(regex_pattern, username):
                if len(username) < 5 or len(username) > 50:
                    raise ValueError
            password = request.form.get("password")
            if username != "" and password != "":
                hashed_password = generate_password_hash(password)
                user = {"username": username, "password": hashed_password, "is_admin":False}
                username_already_exists = pymongo.db.users.find_one(
                    {"username": username}
                )
                if not username_already_exists:
                    db_insert = pymongo.db.users.insert_one(user)
                    # If insert into database is successful, add user to session and redirect
                    if db_insert.acknowledged:
                        session["user"] = str(db_insert.inserted_id)
                        flash("Welcome to The Cupcake Club!")
                        if next_endpoint:
                            return redirect(url_for(next_endpoint))
                        return redirect(url_for("home"))
                    else:
                        flash(GENERIC_ERROR_MESSAGE)
                else:
                    flash("That username is taken, please try another.")
        except Exception:
            flash(GENERIC_ERROR_MESSAGE)
    return render_template(
        "pages/authentication.html",
        auth_mode="Register",
        current_auth_link=current_auth_link,
        alternative_auth_mode="Login",
        alternative_auth_prompt="Already a member? ",
        alternative_auth_link=alternative_auth_link,
    )


@app.route("/logout")
def logout():
    if bool("user" in session):
        del session["user"]
    return redirect(url_for('home'))


@app.route("/create-recipe", methods=["GET", "POST"])
def new_recipe():
    if not bool("user" in session):
        return redirect(url_for("login", next=request.endpoint))
    if request.method == "POST":
        # validate the user input
        try:
            regex_pattern = re.compile(ALPHANUMERICAL_AND_SPACES_REGEX_STRING)
            ingredients = []
            instructions = []
            for key, value in request.form.items():
                if key == "name":
                    if regex_pattern_check(regex_pattern, value):
                        recipe_name = value
                        if len(recipe_name) < 5 or len(recipe_name) > 50:
                            raise ValueError
                if key.startswith("ingredient"):
                    if regex_pattern_check(regex_pattern, value):
                        ingredients.append(value)
                if key.startswith("instruction"):
                    if regex_pattern_check(regex_pattern, value):
                        instructions.append(value)
                if key == "radio":
                    color = value.replace("#", "")

            # check all input values have been provided for valid recipe
            if len(ingredients) == 0 or len(instructions) == 0 or recipe_name is None or color is None:
                raise ValueError
        except ValueError:
            flash(INPUT_FORMAT_ERROR_MESSAGE)
            # return a blank form if invalid
            return render_template("pages/edit-recipe.html", recipe_color=DEFAULT_RECIPE_COLOR)

        try:
            recipe = {
                "name": recipe_name,
                "ingredients": ingredients,
                "instructions": instructions,
                "color": color,
                "author": session["user"],
                "created_at": datetime.now()
            }
            db_insert = pymongo.db.recipes.insert_one(recipe)
            if db_insert.acknowledged:
                return(redirect(url_for('recipe_details', recipe_id=str(db_insert.inserted_id))))
            flash("Recipe could not be created")
        except Exception:
            flash(GENERIC_ERROR_MESSAGE)
            # Return the user with a blank form for safety (if frontend/backend validation checks failed)
            return render_template("pages/edit-recipe.html", recipe_color=DEFAULT_RECIPE_COLOR)
    return render_template("pages/edit-recipe.html", recipe_color=DEFAULT_RECIPE_COLOR)

@app.route("/edit-recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if not bool("user" in session):
        return redirect(url_for("login", next=request.endpoint))
    try:
        db_recipe = pymongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
        db_recipe_name = db_recipe["name"]
        db_ingredients = db_recipe["ingredients"]
        if len(db_ingredients) > 0:
            db_ingredients = ",".join(db_ingredients)
        db_instructions = db_recipe["instructions"]
        if len(db_instructions) > 0:
            db_instructions = ",".join(db_instructions)
        db_color = db_recipe["color"]
    except Exception:
        flash(GENERIC_ERROR_MESSAGE)
        return render_template("pages/edit-recipe.html", recipe_color=DEFAULT_RECIPE_COLOR)

    try:
        user = pymongo.db.users.find_one({"_id":ObjectId(session["user"])})
        if not session["user"] == db_recipe["author"] and not user["is_admin"]:
            flash("You can only edit your own recipes.")
            return redirect(url_for("recipes"))
    except Exception:
        flash(GENERIC_ERROR_MESSAGE)
        return redirect(url_for("recipes"))
    if request.method == "POST":
        # validate the user input
        try:
            regex_pattern = re.compile(ALPHANUMERICAL_AND_SPACES_REGEX_STRING)
            ingredients = []
            instructions = []
            for key, value in request.form.items():
                if key == "name":
                    if regex_pattern_check(regex_pattern, value):
                        recipe_name = value
                        if len(recipe_name) < 5 or len(recipe_name) > 50:
                            raise ValueError
                if key.startswith("ingredient"):
                    if regex_pattern_check(regex_pattern, value):
                        ingredients.append(value)
                if key.startswith("instruction"):
                    if regex_pattern_check(regex_pattern, value):
                        instructions.append(value)
                if key == "radio":
                    color = value.replace("#", "")

            # check all input values have been provided for valid recipe
            if len(ingredients) == 0 or len(instructions) == 0 or recipe_name is None or color is None:
                raise ValueError
        except ValueError:
            flash(INPUT_FORMAT_ERROR_MESSAGE)
            # Return the user to form with the recipe values from the database for safety (if frontend/backend validation checks failed)
            return render_template("pages/edit-recipe.html", recipe_name=db_recipe_name, recipe_ingredients=db_ingredients, recipe_instructions=db_instructions, recipe_color=db_color)

        try:
            updated_recipe = {
                "name": recipe_name,
                "ingredients": ingredients,
                "instructions": instructions,
                "color": color,
            }
            db_update = pymongo.db.recipes.update_one(db_recipe, {"$set": updated_recipe})
            if db_update.acknowledged:
                flash("Recipe updated")
                return redirect(url_for("recipe_details", recipe_id=recipe_id))
            # if update was not successful
            flash("Recipe could not be updated")
            return redirect(url_for("edit_recipe", recipe_id=recipe_id))
        except Exception:
            flash("Recipe could not be updated")
            return redirect(url_for("edit_recipe", recipe_id=recipe_id))
    return render_template("pages/edit-recipe.html", recipe_name=db_recipe_name, recipe_ingredients=db_ingredients, recipe_instructions=db_instructions, recipe_color=db_color)


@app.route("/recipes")
def recipes():
    recipes = pymongo.db.recipes.find().sort("created_at", -1)
    num_recipes = len(list(recipes.clone()))
    return render_template("layout/recipes.html", recipes=recipes, num_recipes=num_recipes)


@app.route("/recipes/<user_id>")
def user_recipes(user_id):
    try:
        user = pymongo.db.users.find_one({"_id":ObjectId(user_id)})
        recipes = pymongo.db.recipes.find({"author":user_id}).sort("created_at", -1)
        # check length of recipes list
        num_recipes = len(list(recipes.clone()))
    except Exception:
        flash(GENERIC_ERROR_MESSAGE)
        return redirect(url_for("recipes"))
    return render_template("layout/recipes.html", recipes=recipes, num_recipes=num_recipes, username=user["username"])


@app.route("/recipe-details/<recipe_id>")
def recipe_details(recipe_id):
    admin_access = False
    try:
        if bool("user" in session):
            user = pymongo.db.users.find_one({"_id":ObjectId(session["user"])})
            admin_access = user["is_admin"]
        db_recipe = pymongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
        author = pymongo.db.users.find_one({"_id":ObjectId(db_recipe["author"])})
    except Exception:
        flash(GENERIC_ERROR_MESSAGE)
        return redirect(url_for("home"))
    return render_template("components/recipe-details.html", id=db_recipe["_id"], name=db_recipe["name"], ingredients=db_recipe["ingredients"], instructions=db_recipe["instructions"], author_name=author["username"], author_id=db_recipe["author"], admin_access=admin_access)


@app.route("/delete-recipe/<recipe_id>")
def delete_recipe(recipe_id):
    try:
        db_delete = pymongo.db.recipes.delete_one({"_id":ObjectId(recipe_id)})
        if db_delete.acknowledged:
            flash("Recipe has been deleted")
    except Exception:
        flash(GENERIC_ERROR_MESSAGE)
    return(redirect(url_for("recipes")))

if __name__ == "__main__":
    app.run(host=os.environ.get("HOST"), port=os.environ.get("PORT"), debug=os.environ.get("DEBUG"))