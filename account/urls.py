from django.urls import path

from .views import CreateUserView

app_name = 'account'
urlpatterns = [
    path('users/', CreateUserView.as_view()),
]