import requests
from bs4 import BeautifulSoup

provinces = ['Province-1', 'Madhesh', 'Bagmati', 'Gandaki', 'Lumbini', 'Karnali', 'Sudurparschim']
print('Which province are you from?')
for i in range(0, len(provinces)):
    print(f'{i+1}. {provinces[i]}')
pradesh = int(input('> ').strip())

district = input('Well, the problem with using open-source software is finding out how lazy the programmers are. I\'m lazy too and printing out a whole list of 77 districts just for you to type a number seemed like a misuse of processing power. Please state the name of your district.\n> ').strip().lower()

rootUrl = 'https://election.ekantipur.com/'
page = requests.get(f'{rootUrl}/pradesh-{pradesh}/district-{district}?lng=eng')
soup = BeautifulSoup(page.content, 'html.parser')

rslt2079 = soup.select('.election-2079')
rsltConsts = rslt2079[0].select('.col-md-6.col-xl-4')
numOfConsts = len(rsltConsts)

n = int(input(f'{district} has {numOfConsts} constituencies. Which would you like to select?\n> ').strip())

candies = rsltConsts[n-1].find_all('div', 'candidate-wrapper')

for cand in candies:
    print(cand.find('div', 'nominee-name').string, '\t', cand.find_all('a')[-1].string.string.strip(), '\t', cand.find('div','vote-count').string.strip())