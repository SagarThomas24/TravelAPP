from django.shortcuts import render
from .models import Destination

# Create your views here.


dests = Destination.objects.all()
def index(request):
    return render(request, 'index.html',{'dests':dests})
