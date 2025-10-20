import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "change_this_secret"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# placeholder for your Telegram token
TOKEN = "8071518517:AAF3huWVr6uAUXtEN3eW6zvs24C07SnZiKk"
