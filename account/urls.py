from django.urls import path

from .views import CreateUserView, CustomTokenObtainPairView, login_page

app_name = 'account'
urlpatterns = [

    #Регистрация
    path('register/', CreateUserView.as_view()),
    # Аутентификация:
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    #ФРОНТ


    path('in/', login_page, name='login_page')
]
