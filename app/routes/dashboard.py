from flask import Blueprint, render_template
from flask_login import login_required
from app.forms import UsernameForm

bp = Blueprint("dashboard", __name__, url_prefix="/")


@bp.route("/")
@login_required
def index():
    form = UsernameForm()
    if form.validate_on_submit():
        pass
    return render_template("dashboard.html", form=form)
