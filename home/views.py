from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def Home(request):
    return render(request,"home.html")