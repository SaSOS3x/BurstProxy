from django.urls import path
from . import views
#from views import IndexDetailView

urlpatterns = [
    path('', views.startblog, name='blog'),
    path('all/', views.opennewsall),
    path('category/<filter>/', views.opennews),
    path('tag/<filter>/', views.opennews),
    path('all/<news>/', views.opennewsfilterall),
    path('tag/<filter>/<news>/', views.opennewsfilter),
    path('category/<filter>/<news>/', views.opennewsfilter),
    path('new/', views.opennewsfilternew),
    path('latest/', views.opennewsfilterlatest),
    path('popular/', views.opennewsfilterpopular),

    path('new/<news>/', views.newnewsopen),
    path('latest/<news>/', views.latestnewsopen),
    path('popular/<news>/', views.popularnewsopen),
]