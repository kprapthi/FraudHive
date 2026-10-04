# Flask app entry point
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import sys
import os

# Add model folder path
sys.path.append("../model")

from preprocess import preprocess_data

app = Flask(__name__)
CORS(app)

# Load ML model and scaler
model = joblib.load("../model/fraud_model.pkl")
scaler = joblib.load("../model/scaler.pkl")


@app.route("/")
def home():
    return jsonify({"message": "Fraud Detection API Running"})


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    try:
        processed_data = preprocess_data(data, scaler)

        prediction = model.predict(processed_data)[0]
        probability = model.predict_proba(processed_data)[0][1]

        result = {
            "prediction": "Fraud" if prediction == 1 else "Legitimate",
            "fraud_probability": round(float(probability), 4)
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)