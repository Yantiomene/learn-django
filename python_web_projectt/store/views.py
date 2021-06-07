#from django.shortcuts import render
from .models import Album, Artist, Contact, Booking
from django.template import loader
from django.http import HttpResponse #pour convertir les reponses en http

# Create your views here.

# page d'acceuil de store
def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{}<li>".format(album.title) for album in albums]
    message = """<ul>{}<ul>""".format("\n".join(formatted_albums)) 
    template = loader.get_template('store/index.html')
    return HttpResponse(template.render(request=request))

#vue pour lister les albums
def listing(request):
    albums = Album.objects.filter(available=True)
    formatted_albums = ["<li>{}<li>".format(album.title) for album in albums]
    message = """<ul>{}<ul>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

#vue pour les details des albums
def detail(request, album_id):
    id = int(album_id)
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artist.all()])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)


def search(request):
    
    query = request.GET['query']
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains = query)

        if not albums.exists():
            albums = Album.objects.filter(artist__name__icontains = query)
        
        if not albums.exists():
            message = "Oupssssss No album find!!!"
        else:
            albums = ["<li>{}<li>".format(album.title) for album in albums]
            message = """
                We find these albums corresponding to your request! Here they are:
                <ul>
                    {}
                <ul>
            """.format("<li><li>".join(albums))
    
    return HttpResponse(message)