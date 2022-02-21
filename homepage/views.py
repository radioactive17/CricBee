from django.shortcuts import render
from django.utils import timezone
from .models import Recentnews,MatchDetails,TeamDetails
import sys
# Create your views here.

#Saving news in db
sys.path.append(r'C:\Users\jigss\OneDrive\Desktop\College\Python\BeautifulSoup\Cricbee')
import news1 as news


j=news.news_headline[::-1]
for i in j:
    n=Recentnews(headline=i[2],upload_time=i[1],link=i[0],image=i[3])
    n.save()

#Saving match & team details in db
#sys.path.append(r'C:\Users\jigss\OneDrive\Desktop\College\Python\pycricbuzz')
#import scorecard as s

#j=s.details[::-1]
'''for i in j:
    x=MatchDetails(matchid=i[0],srs=i[1],mnum=i[2],type=i[3],mchstate=i[4],status=i[5],venue_name=i[6],venue_location=i[7],toss=i[8],date_modified_md=timezone.now())
    x.save()
    y=TeamDetails(
        matchid=MatchDetails.objects.get(matchid=i[0]),
        team_name1=i[9],runs1=i[10],wickets1=i[11],overs1=i[12],inning_num1=i[13],
        team_name2=i[14],runs2=i[15],wickets2=i[16],overs2=i[17],inning_num2=i[18],
        team_name3=i[19],runs3=i[20],wickets3=i[21],overs3=i[22],inning_num3=i[23],
        team_name4=i[24],runs4=i[25],wickets4=i[26],overs4=i[27],inning_num4=i[28],
        date_modified_td=timezone.now()
        )
    y.save()
'''
def home(request):

    recentnews=Recentnews.objects.all().order_by('-newsid')[:10]
    #scorecard1=MatchDetails.objects.all().order_by('-date_modified_md')[:3]
    #scorecard2=TeamDetails.objects.all().order_by('-date_modified_td')[:3]
    carousel=Recentnews.objects.all().reverse().order_by('newsid')[:3]
    context={
        'recentnews':recentnews,
        #'scorecard1':scorecard1,
        #'scorecard2':scorecard2,
        'carousel':carousel,
    }

    return render(request,'homepage/Home.html',context)


def login(request):
    return render(request,'homepage/login.html')

def signup(request):
    return render(request, 'homepage/signup.html')
