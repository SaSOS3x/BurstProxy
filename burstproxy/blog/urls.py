from django.urls import path
from . import views
#from views import IndexDetailView

urlpatterns = [
    path('', views.startblog, name='blog'),
    path('news', views.opennews, name='news'),
]