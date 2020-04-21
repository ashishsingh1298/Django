from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index, name='index'),
   path('single', views.single, name='single'),
   path('blog', views.blog, name='blog'),
   path('contact_us', views.contact_us, name='contact_us')
]
