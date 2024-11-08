from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def add_album(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        album_form = AlbumForm() 
    return render(request, "add_album.html", {"album_form": album_form})

def edit_album(request, id):
    album = Album.objects.get(pk=id)
    album_form = AlbumForm(instance=album)
    if(request.method == "POST"):
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect("homepage")
    else:
        album_form = AlbumForm(instance=album)
    return render(request, "edit_album.html", {"album_form": album_form})

def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect("homepage")