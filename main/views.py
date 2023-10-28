from django.shortcuts import render
from .models import Worker

# Create your views here.
def home(request):

    workers = {}

    worker = Worker.objects.all()
   

    workers["workers"]= worker

    
    return render(request, "main/index.html", workers)