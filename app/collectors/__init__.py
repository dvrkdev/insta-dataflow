import os

from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

cl = Client()
cl.login_by_sessionid(os.environ.get("SESSION_ID"))


def fetch_profile(username: str):
    try:
        # ! TODO: check username is valid or invalid
        user_data = cl.user_info_by_username(username)
        return user_data.dict()
    except Exception as e:
        return {}
