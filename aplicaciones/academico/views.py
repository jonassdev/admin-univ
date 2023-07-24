from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    print(cursos)
    
    return render(request, 'home.html' , {
        'cursos' : cursos
    })