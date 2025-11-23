import os

from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.types import Comment, Media

load_dotenv()

cl = Client()
cl.login_by_sessionid(str(os.environ.get("SESSION_ID")))

def fetch_profile(username: str) -> dict:
    try:
        user_data = cl.user_info_by_username(username)
        return user_data.dict()
    except Exception as e:
        return {}


def fetch_posts(username: str, limit: int = 10) -> list:
    try:
        user_id: int = int(cl.user_id_from_username(username))
        medias: list[Media] = cl.user_medias(user_id, amount=limit)
        return [m.dict() for m in medias]
    except Exception as e:
        return []

def fetch_comments(media_id: int, limit: int = 20) -> list:
    try:
        comments: list[Comment] = cl.media_comments(str(media_id), amount=limit)
        return [c.dict() for c in comments]
    except Exception as e:
        print(f'Error fetching comments for media {media_id}: {e}')
        return []
