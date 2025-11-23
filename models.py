from sqlalchemy.sql import func

from extensions import db

# ======================
# ACCOUNT
# ======================


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    pk = db.Column(db.String(32), unique=True, nullable=False, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)

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

    posts = db.relationship("Post", back_populates="account", cascade="all, delete")
    comments = db.relationship(
        "Comment", back_populates="account", cascade="all, delete"
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


# ======================
# POST
# ======================


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    pk = db.Column(db.String(32), unique=True, nullable=False, index=True)

    account_id = db.Column(
        db.Integer, db.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )

    media_type = db.Column(db.String(20))  # image | video | reel
    caption = db.Column(db.Text)

    like_count = db.Column(db.Integer, default=0)
    comment_count = db.Column(db.Integer, default=0)
    play_count = db.Column(db.Integer, default=0)
    view_count = db.Column(db.Integer, default=0)

    media_url = db.Column(db.String(500))
    thumbnail_url = db.Column(db.String(500))
    duration = db.Column(db.Float)
    location_name = db.Column(db.String(255))

    taken_at = db.Column(db.DateTime(timezone=True))

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    account = db.relationship("Account", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post", cascade="all, delete")

    def __repr__(self):
        return f"<Post {self.pk}>"

    def to_dict(self):
        return {
            "id": self.id,
            "pk": self.pk,
            "account_id": self.account_id,
            "media_type": self.media_type,
            "caption": self.caption,
            "like_count": self.like_count,
            "comment_count": self.comment_count,
            "play_count": self.play_count,
            "view_count": self.view_count,
            "media_url": self.media_url,
            "thumbnail_url": self.thumbnail_url,
            "duration": self.duration,
            "location_name": self.location_name,
            "taken_at": self.taken_at.isoformat() if self.taken_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


# ======================
# COMMENT
# ======================


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    pk = db.Column(db.String(32), unique=True, nullable=False, index=True)

    post_id = db.Column(
        db.Integer, db.ForeignKey("posts.id", ondelete="CASCADE"), nullable=False
    )

    account_id = db.Column(
        db.Integer, db.ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )

    text = db.Column(db.Text)
    like_count = db.Column(db.Integer, default=0)
    has_liked = db.Column(db.Boolean, default=False)

    status = db.Column(db.String(32))  # Active | Hidden | Deleted
    content_type = db.Column(db.String(32))  # default = comment

    created_at_utc = db.Column(db.DateTime(timezone=True))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    account = db.relationship("Account", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"<Comment {self.pk}>"

    def to_dict(self):
        return {
            "id": self.id,
            "pk": self.pk,
            "post_id": self.post_id,
            "account_id": self.account_id,
            "text": self.text,
            "like_count": self.like_count,
            "has_liked": self.has_liked,
            "status": self.status,
            "content_type": self.content_type,
            "created_at_utc": (
                self.created_at_utc.isoformat() if self.created_at_utc else None
            ),
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
