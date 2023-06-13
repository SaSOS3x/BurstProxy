import datetime 
from django.shortcuts import render
from asyncio import Task, tasks
from pickle import NONE
from xml.dom import NotFoundErr
from xml.etree.ElementInclude import include
from django.http import HttpResponse
from .models import News, Categories, Tags, Ip
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.db.models import Count



def startblog(request):
    return redirect('/blog/all')

#ПОКАЗЫВАЕТ ВСЕ НОВОСТИ ПО ТЕГУ И КАТЕГОРИЯМ
def opennews(request, filter):
    categories = Categories.objects.all()
    tag = Tags.objects.all()
    if filter == 'all':
        news = News.objects.all()
        return render(request, 'blog/mainblog.html', {'news': news, 'categories': categories,
                                                    'tag': tag})
    else:
        #КЕЙС ОГРОМНЫЙ, ПИШУ БЭК
        match filter:
            #ПО КАТЕГОРИЯМ
            case "categories_arbitraj":
                news = News.objects.filter(categories_arbitraj = 1)
            case "categories_nocontent":
                news = News.objects.filter(categories_nocontent = 1)
            case "categories_mobileproxy":
                news = News.objects.filter(categories_mobileproxy = 1)
            case "categories_settingsproxy":
                news = News.objects.filter(categories_settingsproxy = 1)
            case "categories_aboutproxy":
                news = News.objects.filter(categories_aboutproxy = 1)
            case "categories_moneysystem":
                news = News.objects.filter(categories_moneysystem = 1)
            case "categories_tarifs":
                news = News.objects.filter(categories_tarifs = 1)
            #ПО ТЕГАМ
            case "tag_firefox":
                news = News.objects.filter(tag_firefox = 1)
            case "tag_Opera":
                news = News.objects.filter(tag_Opera= 1)
            case "tag_tarifs":
                news = News.objects.filter(tag_tarifs = 1)
            case "tag_multiport":
                news = News.objects.filter(tag_multiport = 1)
            case "tag_yandex":
                news = News.objects.filter(tag_yandex = 1)
        try:
            return render(request, 'blog/mainblog.html', {'news': news, 'categories': categories,
                                                        'tag': tag})
        except Exception as e:
            return redirect('/404')

#ПОКАЗЫВАЕТ ВСЕ НОВОСТИ
def opennewsall(request):
    categories = Categories.objects.all()
    tag = Tags.objects.all()
    news = News.objects.all()
    
    return render(request, 'blog/mainblog.html', {'news': news, 'categories': categories,
                                                'tag': tag})
#ПО ТЕГАМ И КАТЕГОРИЯМ ОТКРЫВАЕТ НОВОСТЬ
def opennewsfilter(request, filter, news):

    viewplus(request, news)

    if filter[0:3] == 'tag':
        name = 'tag/'
    else:
        name = 'category/'

    back = 'blog/' + name + filter
    return render(request, 'blog/news/' + news + '.html', {'back': back})

#ОТКРЫВАЕТ НОВОСТЬ ПО all
def opennewsfilterall(request, news):
    viewplus(request, news)
    back = 'blog/all'
    return render(request, 'blog/news/' + news + '.html', {'back': back})

#ФИЛЬТРУЕТ ПО ДАТЕ: НОВЫЕ
def opennewsfilternew(request):
    now = datetime.datetime.now()
    categories = Categories.objects.all()
    tag = Tags.objects.all()
    news = News.objects.filter(date__lt=now).order_by('date')
    return render(request, 'blog/mainblog.html', {'news': news, 'categories': categories,
                                                'tag': tag})

#ФИЛЬТРУЕТ ПО ДАТЕ: СТАРЫЕ
def opennewsfilterlatest(request):
    now = datetime.datetime.now()
    categories = Categories.objects.all()
    tag = Tags.objects.all()
    news = News.objects.filter(date__lt=now).order_by('-date')
    return render(request, 'blog/mainblog.html', {'news': news, 'categories': categories,
                                                'tag': tag})

#ПОКАЗЫВАЕТ ПОПУЛЯРНЫЕ
def opennewsfilterpopular(request):
    news = News.objects.order_by('-view_count')
    categories = Categories.objects.all()
    tag = Tags.objects.all()
    return render(request, 'blog/mainblog.html', {'news': news, 'categories': categories,
                                                'tag': tag})

# ОТКРЫВАЕТ НОВЫЕ
def newnewsopen(request, news):
    viewplus(request, news)
    back = 'blog/new'
    return render(request, 'blog/news/' + news + '.html', {'back': back})

# ОТКРЫВАЕТ СТАРЫЕ
def latestnewsopen(request, news):
    viewplus(request, news)
    back = 'blog/latest'
    return render(request, 'blog/news/' + news + '.html', {'back': back})

# ОТКРЫВАЕТ ПОПУЛЯРНЫЕ
def popularnewsopen(request, news):
    viewplus(request, news)
    back = 'blog/popular'
    return render(request, 'blog/news/' + news + '.html', {'back': back})

def viewplus(request, news):
    id__view = News.objects.get(include_templates = news)
    # id__view = News.objects.filter(include_templates = news)

    ips = get_client_ip(request)

    if Ip.objects.filter(ip=ips).exists():
        id__view.view_id.add(Ip.objects.get(ip=ips))
        id__view.save()
        id__view.view_count = News.total_views(id__view)
        id__view.save()
    else:
        Ip.objects.create(ip=ips)
        id__view.view_id.add(Ip.objects.get(ip=ips))
        id__view.save()
        id__view.view_count = News.total_views(id__view)
        id__view.save()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip

