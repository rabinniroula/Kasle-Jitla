import requests
from bs4 import BeautifulSoup

rootUrl = 'https://election.ekantipur.com/'
page = requests.get(f'{rootUrl}/pradesh-1/district-jhapa?lng=eng')
soup = BeautifulSoup(page.content, 'html.parser')

rslt2079 = soup.select('.election-2079')
rsltConsts = rslt2079[0].select('.col-md-6.col-xl-4')
numOfConsts = len(rsltConsts)

n = int(input(f"Jhapa has {numOfConsts} constituencies. Which would you like to select?\n> ").strip())

candies = rsltConsts[n-1].find_all('div', 'candidate-wrapper')

for cand in candies:
    print(cand.find('div', 'nominee-name').string, '\t', cand.find_all('a')[-1].string.string.strip(), '\t', cand.find('div','vote-count').string.strip())