# infra/comments/app.py
from flask import Flask, request, render_template, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_PATH = "comments.db"

# DB инициализация
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dashboard_id INTEGER NOT NULL,
            author TEXT NOT NULL,
            text TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            is_owner INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/comments", methods=["GET", "POST"])
def comments():
    dashboard_id = request.args.get("dashboard_id")
    if not dashboard_id:
        return "Missing dashboard_id", 400

    if request.method == "POST":
        author = request.form.get("author")
        text = request.form.get("text")
        is_owner = int(request.form.get("is_owner") == "on")
        timestamp = datetime.now().isoformat(" ", "seconds")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comments (dashboard_id, author, text, timestamp, is_owner) VALUES (?, ?, ?, ?, ?)",
                       (dashboard_id, author, text, timestamp, is_owner))
        conn.commit()
        conn.close()
        return redirect(f"/comments?dashboard_id={dashboard_id}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT author, text, timestamp, is_owner FROM comments WHERE dashboard_id = ? ORDER BY timestamp DESC", (dashboard_id,))
    comments = cursor.fetchall()
    conn.close()
    return render_template("index.html", comments=comments, dashboard_id=dashboard_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
