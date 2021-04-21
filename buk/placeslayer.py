import os
from .models import places
from django.contrib.gis.utils import LayerMapping


# Auto-generated `LayerMapping` dictionary for places model
places_mapping = {
    'objectid': 'OBJECTID',
    'state_code': 'state_code',
    'source': 'source',
    'name': 'name',
    'alt_name': 'alt_name',
    'ward_code': 'ward_code',
    'is_primary': 'is_primary',
    'global_id': 'global_id',
    'geom': 'MULTIPOINT',
}


pls  = os.path .abspath(os.path.join(os.path.dirname(__file__), 'places/places.shp'))

def run(verbose=True):
    #variable name = LayerMapping(model_name, path_name, dic_name, transform=True, using='default)
    #variable name.save(strict=True, verbose=True, progress=True)
    place = LayerMapping(places, pls, places_mapping, transform=True, using='default')
    place.save(strict=True, verbose=True, progress=True)