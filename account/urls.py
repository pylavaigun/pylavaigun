from django.urls import path

from .views import CreateUserView, CustomTokenObtainPairView

app_name = 'account'
urlpatterns = [
    path('register/', CreateUserView.as_view()),
    # Аутентификация:
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
