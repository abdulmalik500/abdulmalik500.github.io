from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from buk.models import places

# Create your views here.


def index(request):
    place = places.objects.all() 
    return render(request, 'buk/index.html', {'place': place})

def detail(request, slug=None):
    place = get_object_or_404(Places, slug=slug)
    return render(request, 'buk/detail.html', {'place': place})  
 

#class HomePageView(TemplateView):
 #   template_view = 'buk/index.html'
