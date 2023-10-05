from django.urls import path

from .views import CreateUserView

app_name = 'account'
urlpatterns = [
    path('register/', CreateUserView.as_view()),
]