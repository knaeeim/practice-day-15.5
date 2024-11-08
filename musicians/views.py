from django.shortcuts import render
from album_info.models import Album

def home(request):
    albums = Album.objects.all()
    # print(albums.musician)
    # print(albums.musician.first_name)
    # print(albums.musician.last_name)
    # print(albums.musician.email)
    return render(request, 'home.html', {'albums': albums})