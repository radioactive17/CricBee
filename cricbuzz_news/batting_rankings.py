from bs4 import BeautifulSoup
import requests

source=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/test/batting').text
soup=BeautifulSoup(source,'lxml')

s=soup.find('section',class_='rankings-block__container')
filter=s.table.tbody

#BATSMAN RANKINGS IN TEST
batting_test=[[] for _ in range(100)]
p=0
for i in filter.find_all('tr',class_='table-body'):
    for j in i.find_all('td',class_='table-body__cell'):
        batting_test[p].append(j.text)
    p=p+1

del batting_test[0]

#FOR NO1 BATSMAN
position=filter.tr.find('td',class_='table-body__cell table-body__cell--position').text
position=position.replace("\n","").lstrip(" ").rstrip(" ")

name=filter.tr.find('td',class_='table-body__cell rankings-table__player').find('div',class_='name').text

country=filter.tr.find('td',class_='table-body__cell rankings-table__player').find('div',class_='nationality-logo').text
country=country.replace("\n","").lstrip(" ").rstrip(" ")

rating=filter.tr.find('td',class_='rating').text

batting_test.insert(0,[position,name,country,rating])

#NO1 BATSMAN IS INCLUDED
for i in range(len(batting_test)):
    batting_test[i][0]=batting_test[i][0].replace("\n","").lstrip(" ").rstrip(" ")
    batting_test[i][1]=batting_test[i][1].replace("\n","").lstrip(" ").rstrip(" ")
    batting_test[i][2]=batting_test[i][2].replace("\n","").lstrip(" ").rstrip(" ")

for i in batting_test:
    print(i)
