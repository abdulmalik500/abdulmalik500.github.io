import os
from .models import road
from django.contrib.gis.utils import LayerMapping



# Auto-generated `LayerMapping` dictionary for road model
road_mapping = {
    'state_code': 'state_code',
    'source': 'source',
    'name': 'name',
    'surface_ty': 'surface_ty',
    'smoothness': 'smoothness',
    'one_way': 'one_way',
    'osm_class': 'osm_class',
    'road_class': 'road_class',
    'global_id': 'global_id',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING',

}

rd  = os.path .abspath(os.path.join(os.path.dirname(__file__), 'roads/bukRD_Clip.shp'))

def run(verbose=True):
    rds = LayerMapping(road, rd, road_mapping, transform=True, using='default')
    rds.save(strict=True, verbose=True, progress=True)


# LayerMapping API..
    #model, data_source, mapping, layer=0, source_srs=None, encoding=None, 
    #transaction_mode='commit_on_success', transform=True, unique=True, using='default'

    #encoding="iso-8859-1
    #strict=True, verbose=True