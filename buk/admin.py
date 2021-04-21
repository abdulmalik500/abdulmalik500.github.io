from django.contrib import admin
#from leaflet.admin import LeafletGeoAdmin
from django.contrib.gis import admin
from . models import road, places, boundary

# Register your models here.

@admin.register(road)
class RoadsAdmin(admin.OSMGeoAdmin):
    list_display = ('surface_ty', 'name', 'road_class')

@admin.register(places)
class PlacesAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'source', 'ward_code')

@admin.register(boundary)
class boundsAdmin(admin.OSMGeoAdmin):
    list_display = ('geom', 'id')




#admin.site.register(road)

#class RoadsAdmin(LeafletGeoAdmin):
 #   list_display = ('surface_ty', 'name')

#admin.site.register(road, RoadsAdmin)