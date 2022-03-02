import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# http://localhost:8000/base


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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("A form has been submitted")
        pass
    # "http://localhost:8000/login"
    return render_template(
        "pages/authentication.html",
        auth_mode="Login",
        alternative_auth_mode="Register",
        alternative_auth_prompt="Create an account",
        alternative_auth_link=url_for("register")
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pass
    return render_template(
        "pages/authentication.html",
        auth_mode="Register",
        alternative_auth_mode="Login",
        alternative_auth_prompt="Already a member?",
        alternative_auth_link=url_for("login")
    )


if __name__ == "__main__":
    app.run(host="localhost", port="8000", debug=True)
