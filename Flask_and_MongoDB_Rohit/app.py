from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)


mongo_uri = os.getenv("MONGO_URI")

client = None
collection = None

try:
    if not mongo_uri:
        raise ValueError("MONGO_URI is not configured in .env file")

    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)

    client.admin.command("ping")

    db = client["flask_assignment"]
    collection = db["submissions"]

    print("MongoDB Atlas connected successfully!")

except Exception as e:
    print("MongoDB connection error:", e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():

    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template(
            "index.html",
            error="All fields are required.",
            name=name,
            email=email,
            message=message
        )

    if collection is None:
        return render_template(
            "index.html",
            error="MongoDB connection is not available.",
            name=name,
            email=email,
            message=message
        )

    try:

        document = {
            "name": name,
            "email": email,
            "message": message
        }

        collection.insert_one(document)

        return redirect(url_for("success"))

    except Exception as e:
        return render_template(
            "index.html",
            error=f"Error submitting data: {str(e)}",
            name=name,
            email=email,
            message=message
        )
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)