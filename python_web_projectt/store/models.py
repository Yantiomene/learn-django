from django.db import models

# Create your models here.

ARTISTS = {
    'tenor': {'name': 'Tenor'},
    'aveiro-djess': {'name': 'Aveiro Djess'},
    'daphne': {'name': 'Daphne'},
    'locko': {'name': 'Locko'}
}


ALBUM = [
    {'name': 'Fiang', 'artists': [ARTISTS['tenor']]},
    {'name': 'Nyama', 'artists': [ARTISTS['aveiro-djess']]},
    {'name': 'Amour', 'artists': [ARTISTS['daphne'], ARTISTS['locko']]}
]