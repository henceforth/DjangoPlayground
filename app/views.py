# Create your views here.
from django.shortcuts import render, redirect
from app.models import Picture, Comments
from django.template import Context
from django.forms import ModelForm

class FileForm(ModelForm):
    class Meta:
        model = Picture

def index(request):
    pics = Picture.objects.all()


    return render(request, "index.html", {"pics": pics})

def add(request):
    form_errors = None
    if request.method == 'POST':
        #form
        f = FileForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect("/index")
        else:
            form_errors = f.errors

    ff = FileForm()
    return render(request, "add.html", Context({"form":ff, "form_errors": form_errors}))


