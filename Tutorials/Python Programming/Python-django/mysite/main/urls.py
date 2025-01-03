"""
    Paths to different webpages (endpoints)
    - URLS to different views...
    
    Which view to go to based on URL path
"""

from django.urls import path
from . import views

"""
    root direction -> views.index page (name is index)
"""
urlpatterns = [
    path('<str:name>', views.index, name = 'index'),
]