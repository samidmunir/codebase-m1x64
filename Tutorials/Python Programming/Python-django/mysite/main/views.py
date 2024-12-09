from django.shortcuts import render
from django.http import HttpResponse

"""
    Store all the views for the application.
    - Like a webpage
    - holds all the code that serves HTTP requests
"""

# Create your views here.

def index(response):
    return HttpResponse('<h1>Hello world! - index</h1>')