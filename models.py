from sqlalchemy.sql import func

from extensions import db


class Account(db.Model):
    __tablename__ = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    pk = db.Column(db.String(32), unique=True, nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    full_name = db.Column(db.String(128))
    biography = db.Column(db.Text)
    profile_pic_url = db.Column(db.String(500))
    profile_pic_url_hd = db.Column(db.String(500))
    follower_count = db.Column(db.Integer, default=0)
    following_count = db.Column(db.Integer, default=0)
    media_count = db.Column(db.Integer, default=0)
    is_private = db.Column(db.Boolean, default=False)
    is_verified = db.Column(db.Boolean, default=False)
    account_type = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"<Account {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "pk": self.pk,
            "username": self.username,
            "full_name": self.full_name,
            "biography": self.biography,
            "profile_pic_url": self.profile_pic_url,
            "profile_pic_url_hd": self.profile_pic_url_hd,
            "follower_count": self.follower_count,
            "following_count": self.following_count,
            "media_count": self.media_count,
            "is_private": self.is_private,
            "is_verified": self.is_verified,
            "account_type": self.account_type,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
