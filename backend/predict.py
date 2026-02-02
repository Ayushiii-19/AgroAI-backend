import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("crop_model.h5")

# Class names (must match folder names exactly)
class_names = ["maize", "rice", "wheat"]

print("\n🌱 AI Crop Predictor Ready!\n")

# Ask user for image path
img_path = input("Enter full image path: ")

# Load and prepare image
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array)
predicted_class = class_names[np.argmax(prediction)]

print("\n✅ Predicted Crop:", predicted_class)
