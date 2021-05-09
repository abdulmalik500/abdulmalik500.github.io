#from django.conf.urls import path
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MarkersMapView
from .views import BoundaryMapView
from .views import PlacesMapView

urlpatterns = [
    path('road/', MarkersMapView.as_view()),
    path('', BoundaryMapView.as_view()),
    path('places/', PlacesMapView.as_view()),
    
]