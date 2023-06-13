from django.shortcuts import render
import requests
from asyncio import Task, tasks
from pickle import NONE
from xml.dom import NotFoundErr
from xml.etree.ElementInclude import include
from django.http import HttpResponse
from django.shortcuts import redirect

def start(request):
    return render(request, 'main/index.html')

def nofound404(request):
    return render(request, 'blog/404.html')
