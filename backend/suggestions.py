disease_info = {
    "Tomato___Late_blight": "Use Mancozeb fungicide, avoid overhead watering.",
    "Tomato___Septoria_leaf_spot": "Use chlorothalonil spray weekly.",
    "Potato___Early_blight": "Use Azoxystrobin fungicide and crop rotation.",
    "Corn___Common_rust": "Use resistant hybrids and fungicide.",
    "Healthy": "Plant is healthy! Maintain regular care."
}

def get_suggestion(disease):
    return disease_info.get(disease,"No suggestion available.")
