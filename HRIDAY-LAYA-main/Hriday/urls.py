from django.contrib import admin
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Django Admin Panel
    path("admin/", admin.site.urls),  # Corrected admin path

    # Webpages
    path("", views.home, name="home"),  # Default home page
    path("patient/", views.patient, name="patient"),  # Corrected path
    path("admin-login/", views.adminlogin, name="adminlogin"),  # Corrected path
    path("doctor/", views.doctor, name="doctor"),  # Corrected path
    path("video-call/", views.video_call, name="video_call"),  # Corrected path
    path("home/", views.home, name="home"),  # Corrected path
    path("health-data/", views.health_data, name="health_data"),  # Corrected path
    path("recommendation-dashboard/", views.recommendation_dashboard, name="recommendation_dashboard"),  # Corrected path
    path("food-recommendation/", views.food_recommendation, name="food_recommendation"),  # Corrected path
    path("location-recommendation/", views.location_recommendation, name="location_recommendation"),  # Corrected path
    path("patient-signup/", views.patient_signup, name="patient_signup"),  # Corrected path
    path("doctor-signup/", views.doctor_signup, name="doctor_signup"),  # Corrected path
    path("doctor-dashboard/", views.doctor_dashboard, name="doctor_dashboard"),  # Corrected path
    path("patient-list/", views.patient_list, name="patient_list"),  # Corrected path
    path("emergency-cases/", views.emergency_cases, name="emergency_cases"),  # Corrected path

    # Prediction Routes
    path("prediction/", views.predict, name="predict"),  # Form-based prediction
    path("api/predict/", views.predict_heart_disease, name="predict_heart_disease"),  # API endpoint
]
