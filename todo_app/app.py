from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    with sqlite3.connect("todo.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        """)
init_db()

# Show tasks
@app.route("/")
def index():
    with sqlite3.connect("todo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
    return render_template("index.html", tasks=tasks)

# Add a new task
@app.route("/add", methods=["POST"])
def add():
    content = request.form.get("content")
    if content:
        with sqlite3.connect("todo.db") as conn:
            conn.execute("INSERT INTO tasks (content) VALUES (?)", (content,))
    return redirect(url_for("index"))

# Delete a task
@app.route("/delete/<int:task_id>")
def delete(task_id):
    with sqlite3.connect("todo.db") as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

