from flask import Flask, render_template
from threading import Thread
import bot_core          # your Telegram bot logic
from models import db

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

@app.route("/")
def index():
    return render_template("dashboard.html")

def run_bot():
    """run the Telegram bot loop"""
    bot_core.run_bot()

if __name__ == "__main__":
    Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=10000)
  
