from bs4 import BeautifulSoup
import urllib

links = open('linki_stonoga.txt','r')

for line in links:
    #getting number of views
    url = line
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html,'lxml')
    tag = soup.find(itemprop = 'interactionCount')
    int_count = tag.get('content')

    #finding title of video
    name = soup.find(name = 'title')
    title = soup.title.string
    print title,': ',int_count
