from sqlalchemy.sql import func
from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    joined_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<User ({self.id}) ({self.username})>'