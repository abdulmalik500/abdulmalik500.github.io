#from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
import os
import folium
import json
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from buk.models import places
from buk.models import road
from buk.models import boundary

# Create your views here.



class MarkersMapView(TemplateView):
    template_name = 'buk/index.html'
    def get_context_data(self, **kwargs):
    #Return the view context data.
        context = super().get_context_data(**kwargs)
        context["rd"] = json.loads(serialize("geojson", road.objects.all()))
        #context["plc"] = json.loads(serialize("geojson", places.objects.all()))
        return context


class PlacesMapView(TemplateView):
    template_name = 'buk/index.html'
    def settlements(self, *args, **kwargs):
    #Return the view context data.
        context = super().settlements(*args, **kwargs)
        #context["rd"] = json.loads(serialize("geojson", road.objects.all()))
        context["plc"] = json.loads(serialize("geojson", places.objects.all()))
        return context


class BoundaryMapView(TemplateView):
    template_name = 'buk/index.html'
    def get_context_data(self, **kwargs):
    #Return the view context data.
        context = super().get_context_data(**kwargs)
        #context["rd"] = json.loads(serialize("geojson", road.objects.all()))
        context["bound"] = json.loads(serialize("geojson", boundary.objects.all()))
        return context


#def index(request):
    #context = {}
    #plc = places.objects.all()
    #plc = json.loads(serialize("geojson", places.objects.all()))
    #return context
 #   plc = serialize('geojson', places.objects.all())
   # return render(request, 'buk/index.html', context)
 #   return HttpResponse(plc, content_type = 'json')
    #return HttpResponse(plc, content_type = 'buk/index.html') #it downloads the json

#def detail(request, slug=None):
    #place = get_object_or_404(Places, slug=slug)
    #return render(request, 'buk/detail.html', {'place': place})  
 
def place(request):
    plc = serialize('geojson', places.objects.all())
    return HttpResponse(plc, content_type = 'json')

def roads(request):
    rd = serialize('geojson', road.objects.all())
    return HttpResponse(rd, content_type = 'json')

def boundaries(request):
    bdary = serialize('geojson', boundary.objects.all())
    return HttpResponse(bdary, content_type = 'json')
