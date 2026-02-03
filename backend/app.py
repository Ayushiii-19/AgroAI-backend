from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# HOME ROUTE — TEST SERVER
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "AgroAI Backend Running"})

# PREDICT ROUTE — FRONTEND CALLS THIS
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    # Test response (replace with ML later)
    return jsonify({
        "disease": "Healthy Crop 🌱",
        "confidence": 97.5
    })

# RENDER PORT BINDING
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
