from flask import Flask, render_template
import csv
from stuff import data

app = Flask(__name__)

@app.route("/index")
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
