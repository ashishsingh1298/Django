from django.urls import path

from . import views

urlpatterns = [
    path('hello/',views.index, name='index'),
    path('firstletter/',views.firstletter, name='firstletter'),
    path('lastletter/',views.lastletter, name='lastletter')
]