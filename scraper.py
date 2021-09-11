import requests
from bs4 import BeautifulSoup

class Search():
  def searcher(self, text):
    url = f'http://lndb.info/search?text={text}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id='bodylightnovelscontentid')
    tr = results.find_all('tr')

    slist = []

    for td in tr:
      a = td.find('a')
      b = a['href']
      item = { 'Title': a.text ,'Link':b }
      print(item)
      slist.append(item)

    return slist

Searched = Search()
Searched.searcher('Arifureta')
