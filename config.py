import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "change_this_secret"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# placeholder for your Telegram token
TOKEN = "YOUR_BOT_TOKEN_HERE"
