#from django.shortcuts import render
from .models import ALBUM
from django.http import HttpResponse #pour convertir les reponses en http

# Create your views here.

# page d'acceuil de store
def index(request):
    message = "Hi everyone"
    return HttpResponse(message)

#vue pour lister les albums
def listing(request):
    albums = ["<li>{}<li>".format(album['name']) for album in ALBUM]    
    message = """<ul>{}<ul>""".format("\n".join(albums))
    return HttpResponse(message)

#vue pour les details des albums
def detail(request, album_id):
    id = int(album_id)
    album = ALBUM[id]
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)


def search(request):
    
    query = request.GET['query']
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUM
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Oh zut, we did not find any result !"
        else:
            albums = ["<li>{}<li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête! les voici:
                <ul>
                    {}
                <ul>
            """.format("<li><li>".join(albums))
    
    return HttpResponse(message)