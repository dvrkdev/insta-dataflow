from flask import Blueprint

bp = Blueprint("dashboard", __name__, url_prefix="/")


@bp.route("/")
def index():
    return "index"
