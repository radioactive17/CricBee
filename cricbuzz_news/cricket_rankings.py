from bs4 import BeautifulSoup
import requests

#Test-Rankings
source=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/test').text
soup=BeautifulSoup(source,'lxml')

d=soup.find('div',class_='rankings-block__container rankings-table')    #ranking table for TESTS by ICC
teams_test=[[] for _ in range(12)]
p=0
for i in d.tbody.find_all('tr',class_='table-body'):
    for j in i.find_all('td',class_='table-body__cell'):
        teams_test[p].append(j.text)
    p=p+1
#print(teams_test)
for i in range(12):
    teams_test[i][1]=teams_test[i][1].replace("\n","").lstrip(" ").rstrip(" ")

#print("TEST RANKINGS\n")
#for i in teams_test:
#    print(i)
#print()

#ODI Rankings
source=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').text
soup=BeautifulSoup(source,'lxml')

d=soup.find('div',class_='rankings-block__container rankings-table')    #ranking table for ODI by ICC
teams_odi=[[] for _ in range(20)]
p=0
for i in d.tbody.find_all('tr',class_='table-body'):
    for j in i.find_all('td',class_='table-body__cell'):
        teams_odi[p].append(j.text)
    p=p+1

for i in range(20):
    teams_odi[i][1]=teams_odi[i][1].replace("\n","").lstrip(" ").rstrip(" ")

#print("ODI RANKINGS\n")
#for i in teams_odi:
#    print(i)
#print()

#T20 RANKINGS
source=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/t20i').text
soup=BeautifulSoup(source,'lxml')

d=soup.find('div',class_='rankings-block__container rankings-table')    #ranking table for ODI by ICC
teams_t20=[[] for _ in range(86)]
p=0
for i in d.tbody.find_all('tr',class_='table-body'):
    for j in i.find_all('td',class_='table-body__cell'):
        teams_t20[p].append(j.text)
    p=p+1

for i in range(86):
    teams_t20[i][1]=teams_t20[i][1].replace("\n","").lstrip(" ").rstrip(" ")

#print("T20 RANKINGS\n")
for i in teams_t20:
    print(i)
#print()
