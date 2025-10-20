from flask import Flask, render_template
from threading import Thread
import bot_core
from models import db

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

@app.route("/")
def index():
    return render_template("dashboard.html")

# Function to start the Telegram bot in background
def run_bot():
    try:
        bot_core.run_bot()
    except Exception as e:
        print("Error running bot:", e)

# Start bot when Flask app starts
@app.before_first_request
def activate_bot():
    thread = Thread(target=run_bot)
    thread.daemon = True
    thread.start()
    print("✅ Telegram bot started in background thread")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
