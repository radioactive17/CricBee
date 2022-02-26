from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.cricbuzz.com/cricket-news/latest-news').text
soup = BeautifulSoup(source, 'lxml')

main_div = soup.find('div', class_='cb-col cb-col-67 cb-nws-lft-col')
all_news = [[] for i in range(10)]
i = 0
for news_div in main_div.find_all('div', class_ = 'cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-lg'):

    #fetching img ur
    #img_div = news_div.find('div', class_ = 'cb-col cb-col-33')
    #try:
    #    img_link = img_div.find('img')['src']
    #except:
    #    img_link = img_div.find('img')['source']
    #final_img_link = 'https://www.cricbuzz.com' + str(img_link)
    #print(f'img_url = {final_img_link}')

    #fetching news content
    content = news_div.find('div', class_='cb-col-67 cb-nws-lst-rt cb-col cb-col-text-container')
    topic = content.find('div', class_ = 'cb-nws-time').text
    headline = content.find('h2').text
    link_to_detailed_page = content.find('a')['href']
    final_link_to_detailed_page = 'https://www.cricbuzz.com' + str(link_to_detailed_page)
    intro = content.find('div', class_ = 'cb-nws-intr').text
    time = content.find('span', class_ = 'cb-nws-time').text
    #print(f'topic - {topic}\nheadline - {headline}\nlink - {final_link_to_detailed_page}\nintro - {intro}\ntime - {time}')


    new_source = requests.get(final_link_to_detailed_page).text
    soup1 = BeautifulSoup(new_source, 'lxml')

    #fetching detailed news content
    news = ''
    div = soup1.find('div', class_ = 'cb-col cb-col-67 cb-nws-dtl-lft-col')

    #fetching img url
    try:
        img_link = div.find('section', class_ = 'cb-news-img-section horizontal-img-container').find('img')['src']
    except:
        img_link = div.find('section', class_ = 'cb-news-img-section horizontal-img-container').find('img')['source']
    final_img_link  = 'https://www.cricbuzz.com' + str(img_link)
    
    for c in  div.find_all('section', class_ = 'cb-nws-dtl-itms', itemprop = 'articleBody'):
        news = news + str(c.text) + '\n'
    #print(f'news = {news}')
    all_news[i].extend([topic, headline, intro, time, final_img_link, final_link_to_detailed_page, news])
    #print('\n\n')
    i+= 1

#for i in range(10):
#    print(all_news[i])
