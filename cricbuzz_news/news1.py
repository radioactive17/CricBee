from bs4 import BeautifulSoup
import requests
import urllib.request
import random

source=requests.get("https://www.cricbuzz.com/").text
soup=BeautifulSoup(source,'lxml')

s=soup.find('div',class_='cb-col cb-col-20')
s1=s.find('div',class_='cb-hm-lft')
s2=s1.find_all('div',class_='cb-col-100 cb-lst-itm cb-lst-itm-sm')

# news_headline['link','uploaded time','headline','img src']
news_headline=[[] for _ in range(10)]

p=0
for i in s2:
    # Link to the news
    link=i.find('a').get('href')
    link_final='https://www.cricbuzz.com'+link
    #print(f'link : {link_final}')
    news_headline[p].append(link_final)

    # When it was uploaded
    t=i.div.text
    news_headline[p].append(t)
    #print(f'time : {t}')

    # Headline of news
    unwanted=i.find('div')
    unwanted.extract()
    h=i.text
    #print(f'headline : {h}')
    news_headline[p].append(h)
    p=p+1


p=0
for i in news_headline:
    source=requests.get(news_headline[p][0]).text
    # Image for the news
    soup=BeautifulSoup(source,'lxml')
    if soup.find('img',class_='cursor-pointer'):
        s=soup.find('img',class_='cursor-pointer')
        s1=s.get('src')
        image_url="https://www.cricbuzz.com"+ str(s1)
        news_headline[p].append(image_url)
        #print(s1)
    elif soup.find('iframe',class_='embed-responsive-item'):
        s=soup.find('iframe',class_='embed-responsive-item')
        s1=s.get('src')
        video_url="https://www.cricbuzz.com"+ str(s1)
        news_headline[p].append(news_headline[p-1][3])
        #print(s1)
    p=p+1

for news in news_headline:
    print(news)

'''
p=0
for i in news_headline:
    #file_name=random.randrange(1,100);
    #full_file_name=str(file_name)+'.jpg'
    img_url="https://www.cricbuzz.com"+ str(news_headline[p][3])
    news_headline[p][3]=img_url
    p=p+1

for i in news_headline:
    print(i)
'''
