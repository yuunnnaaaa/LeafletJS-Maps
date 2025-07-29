from django.shortcuts import render
from .models import ServiceArea

def area_map(request):
    areas = ServiceArea.objects.all()
    return render(request, 'area_app/area_map.html', {'areas': areas})

