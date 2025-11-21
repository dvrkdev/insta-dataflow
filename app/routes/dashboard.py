from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required

from app import db
from app.collectors import fetch_profile
from app.forms import UsernameForm
from app.models import Account

bp = Blueprint("dashboard", __name__, url_prefix="/")


@bp.route("/", methods=["POST", "GET"])
@login_required
def index():
    form = UsernameForm()
    if form.validate_on_submit():

        user_data = fetch_profile(form.username.data)
        if user_data:
            account = Account(
                pk=user_data.get("pk"),
                username=user_data.get("username"),
                full_name=user_data.get("full_name"),
                biography=user_data.get("biography"),
                profile_pic_url=user_data.get("profile_pic_url"),
                profile_pic_url_hd=user_data.get("profile_pic_url_hd"),
                follower_count=user_data.get("follower_count"),
                following_count=user_data.get("following_count"),
                media_count=user_data.get("media_count"),
                is_private=user_data.get("is_private"),
                is_verified=user_data.get("is_verified"),
                account_type=user_data.get("account_type"),
            )

            db.session.add(account)
            db.session.commit()

            flash("Account fetched successfully!", "success")
            return redirect(url_for("dashboard.index"))

        flash("Account not found!", "danger")
        return redirect(url_for("dashboard.index"))
    return render_template("dashboard.html", form=form)
