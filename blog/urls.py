from django.urls import path
from .views import home,about

urlpatterns = [
    path('',home,name='blog-home'),
    path('about-this/',about,name='blog-about')
    
]
