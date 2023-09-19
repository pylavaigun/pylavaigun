from django.urls import path
from ml_app import views

urlpatterns = [
    path("", views.index, name="main"),
]