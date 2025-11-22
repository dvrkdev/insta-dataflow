from flask import Blueprint, render_template
from app.models import Account
from flask_login import login_required

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/account/<int:id>')
def index():
    ...