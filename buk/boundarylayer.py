import os
from .models import boundary
from django.contrib.gis.utils import LayerMapping

# Auto-generated `LayerMapping` dictionary for boundary model
boundary_mapping = {
    'id': 'Id',
    'geom': 'MULTIPOLYGON',
}


bound = os.path .abspath(os.path.join(os.path.dirname(__file__), 'boundary/boundary.shp'))

def run(verbose=True):
    #variable name = LayerMapping(model_name, path_name, dic_name, transform=True, using='default)
    #variable name.save(strict=True, verbose=True, progress=True)
    bd = LayerMapping(boundary, bound, boundary_mapping, transform=True, using='default')
    bd.save(strict=True, verbose=True, progress=True)