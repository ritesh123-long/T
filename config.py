# ==============================
# CONFIGURATION FILE
# ==============================

# ⚙️ Telegram Bot Token (replace with your actual token)
token = "YOUR_BOT_TOKEN_HERE"

# 📂 Folder where downloaded files will be stored
output_folder = "downloads"

# 🚫 Max file size allowed (in bytes) — 50MB default
max_filesize = 50 * 1024 * 1024

# 🧠 Enable or disable activity logs to admin panel
enable_logs = True

# 🌐 Flask web panel configuration
flask_secret_key = "super_secret_key_change_this"

# Default admin (you can add more from the panel)
default_admin = {
    "username": "Admin",
    "password": "090411"
}

# 📦 SQLite database filename
database_name = "database.db"
