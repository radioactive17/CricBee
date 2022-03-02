from django.shortcuts import render
from django.utils import timezone
from .models import Recentnews, Fixtures, Fixtures_date
import sys
from cricbuzz.news import *
from cricbuzz.international_fixtures import *
from pytz import timezone
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

#Storing news in the database
def storing_news_in_db():
    news = recent_news()
    #[topic, headline, intro, time, final_img_link, final_link_to_detailed_page, news]
    for rn in news:
        try:
            if Recentnews.objects.get(topic = rn[0], headline = rn[1], intro = rn[2], link = rn[5], image = rn[4], news = rn[6]):
                continue
        except:
            n = Recentnews(topic = rn[0], headline = rn[1], intro = rn[2], upload_time = rn[3], link = rn[5], image = rn[4], news = rn[6])
            n.save()
            print(f'Updating Recentnews....')
    current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f'Checked for new news at {current_time}')

#Fetching and storing news in database every 30 minutes
def news_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(storing_news_in_db, 'interval', minutes = 30)
    scheduler.start()

#storin international fixtures in the database
def storing_int_fixtures_in_db():
    ifixtures = international_fixtures()
    #[date, tour, match, location, time]
    for i in ifixtures:
        try:
            if Fixtures.objects.get(fixture_type = 'international', date = i[0], tour = i[1], match = i[2], location = i[3], time = i[4]):
                continue
        except:
            int_fixture = Fixtures(fixture_type = 'international', date = i[0], tour = i[1], match = i[2], location = i[3], time = i[4])
            int_fixture.save()
            int_fix_date = Fixtures_date(fixture = int_fixture, date = i[0])
            int_fix_date.save()
            print(f'Updating International Fixtures.....')
    current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%ms-%d %H:%M:%S.%f')
    print(f'Checked for updated Fixtures at {current_time}')

#Fetching and storing updated international fixture in database every 24 hours
def int_fixture_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(storing_int_fixtures_in_db, 'interval', hours = 24)
    scheduler.start()

########################################## VIEWS SECTION ##########################################
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
    today = datetime.today()
    date_from, month, year = today.strftime("%d"), today.strftime("%b").upper(), today.strftime("%Y")
    print(f'{date_from} {month} {year}')
    date_to = str(int(date_from) + 2).zfill(2)


    return render(request, 'homepage/fixtures.html')

def login(request):
    return render(request,'homepage/login.html')

def signup(request):
    return render(request, 'homepage/signup.html')
