from django.shortcuts import render


# Главная страница
def index(request):
    template = 'index.html'
    return render(request, template)

# Create your views here.
