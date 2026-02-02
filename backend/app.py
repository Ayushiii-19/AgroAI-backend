import os
import gdown

MODEL_PATH = "crop_model.h5"
MODEL_URL = "PUT_GOOGLE_DRIVE_LINK_HERE"

if not os.path.exists(MODEL_PATH):
    print("Downloading ML model...")
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

print("🌿 Starting AgroAI Backend Server...")

# Load model
model = load_model("crop_model.h5")

# Class labels
CLASS_NAMES = [
    "Apple___Black_rot",
    "Corn___Gray_leaf_spot",
    "Potato___Early_blight",
    "Tomato___Late_blight"
]

@app.route("/")
def home():
    return jsonify({"status": "AgroAI Backend Running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        file = request.files["file"]

        # Convert uploaded file to image
        img = Image.open(io.BytesIO(file.read())).convert("RGB")
        img = img.resize((128, 128))

        # Preprocess image
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        predictions = model.predict(img_array)[0]
        confidence = float(np.max(predictions))
        class_index = int(np.argmax(predictions))
        label = CLASS_NAMES[class_index]

        return jsonify({
            "prediction": label,
            "confidence": round(confidence * 100, 2),
            "treatment": get_treatment(label)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_treatment(label):
    treatments = {
        "Apple___Black_rot": "Prune infected branches, apply fungicide, and avoid overhead watering.",
        "Corn___Gray_leaf_spot": "Use resistant varieties and apply foliar fungicide.",
        "Potato___Early_blight": "Remove infected leaves, apply copper fungicide, ensure proper air circulation.",
        "Tomato___Late_blight": "Destroy infected plants and use preventive fungicide sprays."
    }
    return treatments.get(label, "Maintain crop hygiene and monitor regularly.")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
