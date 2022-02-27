from django.shortcuts import render
from django.utils import timezone
from .models import Recentnews, Fixtures
import sys
from cricbuzz import news, international_fixtures

#Saving news in db
for news in news.all_news[::-1]:
    n = Recentnews(topic = news[0], headline = news[1], intro = news[2], upload_time = news[3], link = news[5], image = news[4], news = news[6])
    n.save()


def home(request):
    recentnews=Recentnews.objects.all().order_by('-newsid')[:6]
    #carousel=Recentnews.objects.all().reverse().order_by('newsid')[:3]
    context={
        'recentnews':recentnews,
        #'carousel':carousel,
    }

    return render(request,'homepage/home.html',context)

def timeline(request):
    return render(request, 'homepage/timeline.html')

def news(request):
    recentnews = Recentnews.objects.all().order_by('-newsid')[:10]
    context = {
        'recentnews': recentnews,
    }
    return render(request, 'homepage/news.html', context)

def detailed_news(request, *arg, **kwargs):
    #print(kwargs['pk'])
    news = Recentnews.objects.get(newsid = kwargs['pk'])
    context = {
        'news' : news,
    }
    return render(request, 'homepage/detailed_news.html', context)

def fixtures(request):
    for fixtures in international_fixtures.int_fixtures[::-1]:
        f = Fixtures(fixture_type = 'international', date = fixtures[0], tour = fixtures[1], match = fixtures[2], location = fixtures[3], time = fixtures[4])
        f. save()
    int_fixtures = Fixtures.objects.filter(fixture_type = 'international').order_by('-fixture_id')
    context = {
        'int_fixtures': int_fixtures,
    }
    return render(request, 'homepage/fixtures.html', context)

def login(request):
    return render(request,'homepage/login.html')

def signup(request):
    return render(request, 'homepage/signup.html')
