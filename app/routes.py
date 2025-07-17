from flask import render_template
import os

from app import app

# === Visitor Counter Logic ===
counter_file = "counter.txt"

def read_count():
    if not os.path.exists(counter_file):
        with open(counter_file, 'w') as f:
            f.write("0")
    with open(counter_file, 'r') as f:
        return int(f.read())

def increment_count():
    count = read_count() + 1
    with open(counter_file, 'w') as f:
        f.write(str(count))
    return count
# =============================

@app.route("/")
def home():
    visit_count = increment_count()
    return render_template("index.html", visit_count=visit_count)
