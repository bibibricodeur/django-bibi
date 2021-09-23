from django.shortcuts import render
# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('<h1>Je suis la page DjangoBibi (home)</h1>')
    return render(request, 'django-bibi/base.html')
