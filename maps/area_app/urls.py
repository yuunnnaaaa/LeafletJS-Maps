from django.urls import path
from . import views

urlpatterns = [
    path('area-map/', views.area_map, name='area_map'),
]
