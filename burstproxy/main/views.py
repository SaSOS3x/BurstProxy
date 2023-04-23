from django.shortcuts import render
import requests
from asyncio import Task, tasks
from pickle import NONE
from xml.dom import NotFoundErr
from xml.etree.ElementInclude import include
from django.http import HttpResponse

def start(request):
    return render(request, 'main/index.html')
# Create your views here.
