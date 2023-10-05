from django.urls import path

from .views import CreateUserView, CustomTokenObtainPairView

app_name = 'account'
urlpatterns = [
    path('register/', CreateUserView.as_view()),
    # Аутентификация:
    path('api/auth/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
