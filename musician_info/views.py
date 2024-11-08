from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def add_musician(request):
    if request.method == "POST":
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
    else:
        musician_form = MusicianForm()
    return render(request, "add_musician.html", {"mus_form" : musician_form})

def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    if request.method == "POST":
        musician_form = MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("homepage")
    else:
        musician_form = MusicianForm(instance=musician)
    return render(request, "edit_musician.html", {"mus_form": musician_form})