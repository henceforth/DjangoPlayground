# Create your views here.
from django.shortcuts import render
from app.models import Picture, Comments
from django.template import Context
from django.forms import ModelForm

class FileForm(ModelForm):
    class Meta:
        model = Picture

def index(request):
    pics = Picture.objects.all()

    return render(request, "index.html", Context({"pics": pics}))

def add(request):
    if request.method == 'POST':
        #form
        f = FileForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("index")
        else:
            #todo: show errors, reload page
            pass

    ff = FileForm()
    return render(request, "add.html", Context({"form":ff}))


