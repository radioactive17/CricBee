from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Recentnews, Fixtures, Fix_Date
import sys
from cricbuzz.news import *
from cricbuzz.international_fixtures import *
from cricbuzz.domestic_fixtures import *
from cricbuzz.womens_fixtures import *
from pytz import timezone
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models import Q
import dateutil.parser #dateutil.parser.parse('2008-04-10 11:47:58-05')
from django.contrib import messages


#Storing news in the database
def storing_news_in_db():
    news = recent_news()
    #[topic, headline, intro, time, final_img_link, final_link_to_detailed_page, news]
    for rn in news:
        try:
            if Recentnews.objects.get(headline = rn[1]):
                pass
        except:
            n = Recentnews(topic = rn[0], headline = rn[1], intro = rn[2], upload_time = rn[3], link = rn[5], image = rn[4], news = rn[6])
            n.save()
            print(f'Updating Recentnews....')
    current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f'Checked for new news at {current_time}')

#Fetching and storing news in database every 30 minutes
def news_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(storing_news_in_db, 'interval', seconds = 90)
    scheduler.start()

#storing international fixtures in the database
def storing_int_fixtures_in_db():
    ifixtures = international_fixtures()
    #[date, tour, match, location, time]
    for i in ifixtures:
        fdate = dateutil.parser.parse(i[0]).strftime("%Y-%m-%d")
        try:
            if Fixtures.objects.get(fixture_type = 'international', date = fdate, tour = i[1], match = i[2], location = i[3], time = i[4]):
                pass
        except:
            int_fixture = Fixtures(fixture_type = 'international', date = fdate, tour = i[1], match = i[2], location = i[3], time = i[4])
            int_fixture.save()
            try:
                if Fix_Date.objects.get(date = fdate):
                    pass
            except:
                fdate = Fix_Date(date = fdate)
                fdate.save()
            print(f'Updating International Fixtures.....')
    current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%ms-%d %H:%M:%S.%f')
    print(f'Checked for updated International Fixtures at {current_time}')

#Fetching and storing updated international fixture in database every 24 hours
def int_fixture_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(storing_int_fixtures_in_db, 'interval', minutes = 1)
    scheduler.start()

#storing domestic fixtures in the database
def storing_dom_fixtures_in_db():
    dfixtures = domestic_fixtures()
    for d in dfixtures:
        fdate = dateutil.parser.parse(d[0]).strftime("%Y-%m-%d")
        try:
            if Fixtures.objects.get(fixture_type = 'domestic', date = fdate, tour = d[1], match = d[2], location = d[3], time = d[4]):
                pass
        except:
            dom_fixture = Fixtures(fixture_type = 'domestic', date = fdate, tour = d[1], match = d[2], location = d[3], time = d[4])
            dom_fixture.save()
            try:
                if Fix_Date.objects.get(date = fdate):
                    pass
            except:
                fdate = Fix_Date(date = fdate)
                fdate.save()
            print(f'Updating Domestic Fixtures........')
    current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%ms-%d %H:%M:%S.%f')
    print(f'Checked for updated Domestic Fixtures at {current_time}')

#Fetching and storing updated domestic fixture in database every 24 hours
def dom_fixture_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(storing_dom_fixtures_in_db, 'interval', minutes = 7)
    scheduler.start()

#storing womens fixtures in the database
def storing_wom_fixtures_in_db():
    wfixtures = womens_fixtures()
    for w in wfixtures:
        fdate = dateutil.parser.parse(w[0]).strftime("%Y-%m-%d")
        try:
            if Fixtures.objects.get(fixture_type = 'womens', date = fdate, tour = w[1], match = w[2], location = w[3], time = w[4]):
                pass
        except:
            wom_fixture = Fixtures(fixture_type = 'womens', date = fdate, tour = w[1], match = w[2], location = w[3], time = w[4])
            wom_fixture.save()
            try:
                if Fix_Date.objects.get(date = fdate):
                    pass
            except:
                fdate = Fix_Date(date = fdate)
                fdate.save()
            print(f'Updating Womens Fixtures........')
    current_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%ms-%d %H:%M:%S.%f')
    print(f'Checked for updated Womens Fixtures at {current_time}')

#Fetching and storing updated womens fixture in database every 24 hours
def wom_fixture_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(storing_wom_fixtures_in_db, 'interval', minutes = 3)
    scheduler.start()

##################################################################### VIEWS SECTION #####################################################################
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

def fixtures(request, *args, **kwargs):
    today = datetime.today().strftime("%Y-%m-%d")
    day3 = datetime.today() + timedelta(days=3)
    day3 = day3.strftime("%Y-%m-%d")
    fixtures = Fixtures.objects.filter(Q(fixture_type = kwargs['fixture_type']) & Q(date__range = (today, day3)))
    fixtures_date = Fix_Date.objects.filter(date__range = (today, day3))
    context = {
        'fixtures': fixtures,
        'fixtures_date': fixtures_date,
    }
    return render(request, 'homepage/fixtures.html', context)
