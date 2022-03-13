import os
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
            username = request.form.get("username").lower()
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
        except Exception as exception:
            flash(GENERIC_ERROR_MESSAGE)
    return render_template(
        "pages/authentication.html",
        auth_mode="Login",
        current_auth_link=current_auth_link,
        alternative_auth_mode="Register",
        alternative_auth_prompt="Create an account",
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
            username = request.form.get("username").lower()
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
        except Exception as exception:
            print(exception)
            flash(GENERIC_ERROR_MESSAGE)
    return render_template(
        "pages/authentication.html",
        auth_mode="Register",
        current_auth_link=current_auth_link,
        alternative_auth_mode="Login",
        alternative_auth_prompt="Already a member?",
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
        try:
            recipe_name = request.form.get("name").lower()
            ingredients = []
            instructions = []
            for key, value in request.form.items():
                if key.startswith("ingredient"):
                    ingredients.append(value)
                if key.startswith("instruction"):
                    instructions.append(value)
            color = request.form.get("radio").replace("#","")

            recipe = {
                "name": recipe_name,
                "ingredients": ingredients,
                "instructions": instructions,
                "color": color,
                "author": session["user"]
            }
            db_insert = pymongo.db.recipes.insert_one(recipe)
            if db_insert.acknowledged:
                return(redirect(url_for('recipe_details', recipe_id=str(db_insert.inserted_id))))
            flash("Recipe could not be created")
        except Exception as exception:
            flash(GENERIC_ERROR_MESSAGE)
    return render_template("pages/edit-recipe.html", recipe_color="e8c0d9")

@app.route("/edit-recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if not bool("user" in session):
        return redirect(url_for("login", next=request.endpoint))
    try:
        db_recipe = pymongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
        ingredients = db_recipe["ingredients"]
        if len(ingredients) > 0:
            ingredients = ",".join(ingredients)
        instructions = db_recipe["instructions"]
        if len(instructions) > 0:
            instructions = ",".join(instructions)
        color = db_recipe["color"]

        user = pymongo.db.users.find_one({"_id":ObjectId(session["user"])})
        if not session["user"] == db_recipe["author"] and not user["is_admin"]:
            flash("You can only edit your own recipes.")
            return redirect(url_for("recipes"))
    except Exception as exception:
        flash(GENERIC_ERROR_MESSAGE)
        return redirect(url_for("recipes"))
    if request.method == "POST":
        try:
            recipe_name = request.form.get("name").lower()
            ingredients = []
            instructions = []
            for key, value in request.form.items():
                if key.startswith("ingredient"):
                    ingredients.append(value)
                if key.startswith("instruction"):
                    instructions.append(value)
            color = request.form.get("radio").replace("#","")
            updated_recipe = {
                "name": recipe_name,
                "ingredients": ingredients,
                "instructions": instructions,
                "color": color,
                "author": session["user"]
            }
            db_update = pymongo.db.recipes.update_one(db_recipe, {"$set": updated_recipe})
            if db_update.acknowledged:
                flash("Recipe updated")
                return redirect(url_for("recipe_details", recipe_id=recipe_id))
            # if update was not successful
            return redirect(url_for("edit_recipe", recipe_id=recipe_id))
        except Exception as exception:
            flash("Recipe could not be updated")
            return redirect(url_for("edit_recipe", recipe_id=recipe_id))
    return render_template("pages/edit-recipe.html", recipe_name=db_recipe["name"], recipe_ingredients=ingredients, recipe_instructions=instructions, recipe_color=color)


@app.route("/recipes")
def recipes():
    recipes = pymongo.db.recipes.find()
    return render_template("layout/recipes.html", recipes=recipes)


@app.route("/recipe-details/<recipe_id>")
def recipe_details(recipe_id):
    try:
        db_recipe = pymongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
        author = pymongo.db.users.find_one({"_id":ObjectId(db_recipe["author"])})
        user = pymongo.db.users.find_one({"_id":ObjectId(session["user"])})
    except Exception as exception:
        flash(GENERIC_ERROR_MESSAGE)
        return redirect(url_for("home"))
    return render_template("components/recipe-details.html", id=db_recipe["_id"], name=db_recipe["name"], ingredients=db_recipe["ingredients"], instructions=db_recipe["instructions"], author_name=author["username"], author_id=db_recipe["author"], admin_access=user["is_admin"])


@app.route("/delete-recipe/<recipe_id>")
def delete_recipe(recipe_id):
    try:
        db_delete = pymongo.db.recipes.delete_one({"_id":ObjectId(recipe_id)})
        if db_delete.acknowledged:
            flash("Recipe has been deleted")
    except Exception as exception:
        flash(GENERIC_ERROR_MESSAGE)
    return(redirect(url_for("recipes")))

if __name__ == "__main__":
    app.run(host=os.environ.get("HOST"), port=os.environ.get("PORT"), debug=os.environ.get("DEBUG"))