from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import joblib
import numpy as np
import json
import os
from django.conf import settings

# Dynamically find the model path
model_path = os.path.join(settings.BASE_DIR, "Hriday", "ml_models", "heart_disease_model.pkl")

# Load model with error handling
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None  # Handle missing model file


# Helper function for prediction
def make_prediction(input_data):
    if model is None:
        raise ValueError("Model file not found")
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return int(prediction[0])  # Convert NumPy value to int


# Home Page
def home(request):
    return render(request, "home.html")


# Patient Page
def patient(request):
    return render(request, "patient.html")


# Admin Login Page
def adminlogin(request):
    return render(request, "adminlogin.html")


# Doctor Page
def doctor(request):
    return render(request, "doctor.html")


# Video Call Page
def video_call(request):
    return render(request, "video_call.html")


def health_data(request):
    return render(request, "health_data.html")


def recommendation_dashboard(request):
    return render(request, "recommendation_dashboard.html")


def food_recommendation(request):
    return render(request, "recomendation.html")


def location_recommendation(request):
    return render(request, "location_recomendation.html")


def patient_signup(request):
    return render(request, "patient_signup.html")


def doctor_signup(request):
    return render(request, "doctor_signup.html")


def doctor_dashboard(request):
    return render(request, "doctor_dashboard.html")


def patient_list(request):
    # Fetch patient data from the database (if needed)
    patients = []  # Replace with actual database query
    return render(request, "patient_list.html", {"patients": patients})


def emergency_cases(request):
    # Fetch emergency cases from the database (if needed)
    emergency_cases = []  # Replace with actual database query
    return render(request, "emergency_cases.html", {"emergency_cases": emergency_cases})


# Prediction Page (Form-based submission)
def predict(request):
    if request.method == "POST":
        try:
            # Extract user input from form
            features = [float(request.POST.get(key, 0)) for key in request.POST.keys()]
            result = make_prediction(features)
            result_text = "Heart Disease Detected" if result else "No Heart Disease"
            return render(request, "prediction.html", {"result": result_text})

        except ValueError as e:
            return render(request, "prediction.html", {"result": f"Error: {str(e)}"})
        except Exception as e:
            return render(request, "prediction.html", {"result": f"Unexpected Error: {str(e)}"})

    return render(request, "prediction.html")


# API Endpoint for Prediction (JSON-based)
@csrf_exempt
def predict_heart_disease(request):
    if request.method == "POST":
        try:
            # Parse JSON data
            data = json.loads(request.body)
            features = data.get("features", [])
            if not features:
                return JsonResponse({"error": "No features provided"}, status=400)

            # Make prediction
            result = make_prediction(features)
            return JsonResponse({"prediction": result})
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected Error: {str(e)}"}, status=500)

    return JsonResponse({"message": "Send a POST request with JSON data."})