from django.shortcuts import render
from django.utils import timezone
from .models import Recentnews, Fixtures, Fixtures_date
import sys
from cricbuzz.news import *
import schedule

#Storing news in the databse
def storing_news_in_db():
    news = recent_news()
    #[topic, headline, intro, time, final_img_link, final_link_to_detailed_page, news]
    for rn in news:
        if Recentnews.objects.get(topic = rn[0], headline = rn[1], intro = rn[2], link = rn[5], image = rn[4], news = rn[6]):
            continue
        else:
            n = Recentnews(topic = rn[0], headline = rn[1], intro = rn[2], time = rn[3], link = rn[5], image = rn[4], news = rn[6])
            n.save()

schedule.every(15).minutes.do(storing_news_in_db)

def home(request):
    #storing_news_in_db()
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
    '''
    for fixtures in international_fixtures.int_fixtures[::-1]:
        f = Fixtures(fixture_type = 'international', date = fixtures[0], tour = fixtures[1], match = fixtures[2], location = fixtures[3], time = fixtures[4])
        d = Fixtures_date(fixture = f, date = fixtures[0])
        f. save()
        d.save()
    int_fixtures = Fixtures.objects.filter(fixture_type = 'international').order_by('fixture_id')
    #print(int_fixtures)
    int_fixtures_date = Fixtures_date.objects.filter(fixture__in = int_fixtures)
    #print(int_fixtures_date)
    context = {
        'int_fixtures': int_fixtures,
        'int_fixtures_date': int_fixtures_date,
    }
    '''
    return render(request, 'homepage/fixtures.html')

def login(request):
    return render(request,'homepage/login.html')

def signup(request):
    return render(request, 'homepage/signup.html')
