from django.urls import path

from .views import CreateUserView, LoginAPIView

app_name = 'account'
urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
