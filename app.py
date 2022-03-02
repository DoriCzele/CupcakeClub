import os
from flask import Flask, render_template

app = Flask(__name__)

# http://localhost:8000/base


@app.route("/base")
def temp_base_test():
    return render_template("layout/base.html")


@app.route("/403")
def temp_403_test():
    return render_template("layout/403.html")


@app.route("/404")
def temp_404_test():
    return render_template("layout/404.html")    


if __name__ == "__main__":
    app.run(host="localhost", port="8000", debug=True)
