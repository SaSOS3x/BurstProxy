from django.shortcuts import render
import requests
from asyncio import Task, tasks
from pickle import NONE
from xml.dom import NotFoundErr
from xml.etree.ElementInclude import include
from django.http import HttpResponse

def startblog(request):
    return render(request, 'blog/mainblog.html')
# Create your views here.
