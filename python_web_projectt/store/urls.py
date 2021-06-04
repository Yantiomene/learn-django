from  django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing), # "/store" appellera la methode "index" dans views.py
    url(r'^(?P<album_id>[0-9]+)/$', views.detail), # sera appelée pour afficher les details des albums
    url(r'^search/$', views.search),
]