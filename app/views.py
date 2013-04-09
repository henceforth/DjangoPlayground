# Create your views here.
from django.shortcuts import render
from app.models import Picture, Comments
from django.template import Context

def index(request):
    pics = Picture.objects.all()

    return render(request, "index.html", Context({"pics": pics}))
