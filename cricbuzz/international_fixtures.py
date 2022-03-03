from bs4 import BeautifulSoup
import requests
import time

def international_fixtures():
    source = requests.get('https://www.cricbuzz.com/cricket-schedule/upcoming-series/international').text
    soup = BeautifulSoup(source, 'lxml')
    main_div = soup.find('div', class_ = 'cb-bg-white cb-schdl cb-col cb-col-100').find('div', id = 'international-list')
    int_fixtures = []
    for content_div in main_div.find_all('div', class_ = 'cb-col-100 cb-col'):
        try:
            date = content_div.find('div', class_ = 'cb-lv-grn-strip text-bold').text
        except:
            pass
        tour = content_div.find('a', class_ = 'cb-col-33 cb-col cb-mtchs-dy text-bold').text
        matches = content_div.find('div', class_ = 'cb-col-67 cb-col')
        for match_details, location in zip(matches.find_all('div', class_ = 'cb-ovr-flo cb-col-60 cb-col cb-mtchs-dy-vnu cb-adjst-lst'), matches.find_all('div', class_ = 'cb-col-40 cb-col cb-mtchs-dy-tm cb-adjst-lst')):
            match = match_details.find('a').text
            location = match_details.find('div', class_ = 'cb-font-12 text-gray cb-ovr-flo').text
            time = content_div.find('div', class_ = 'cb-col-40 cb-col cb-mtchs-dy-tm cb-adjst-lst').text
            temp = [date, tour, match, location, time]
            if temp not in int_fixtures:
                int_fixtures.append(temp)
    #for fixtures in int_fixtures:
    #    for ele in fixtures:
    #        print(ele)
    #    print()
    return int_fixtures

'''
if __name__ == '__main__':
    while True:
        international_fixtures()
        wait = 12
        print(f'Waiting {wait} hours before fetching new fixtures')
        time.sleep(wait * 60 * 60)
'''
