import os

from dotenv import load_dotenv
from flask import Flask, render_template

from extensions import csrf, db

# from models import Account


load_dotenv()

app = Flask(
    __name__, template_folder="templates", static_folder="static", static_url_path="/"
)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
csrf.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
