import os
from flask import Flask, render_template

app = Flask(__name__)

# http://localhost:8000/base


@app.route("/base")
def temp_base_test():
    return render_template("layout/base.html")


if __name__ == "__main__":
    app.run(host="localhost", port="8000", debug=True)
