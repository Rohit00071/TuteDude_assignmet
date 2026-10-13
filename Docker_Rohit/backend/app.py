from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Flask backend is running",
        "service": "Docker Assignment Backend"
    })


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():

    data = request.get_json()

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({
            "error": "Item name and description are required"
        }), 400

    return jsonify({
        "message": "To-Do item submitted successfully",
        "itemName": item_name,
        "itemDescription": item_description
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )