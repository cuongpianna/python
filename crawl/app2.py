import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import multiprocessing

client = MongoClient()
db = client['stackover']
tbl = db['link']


class Crawler(multiprocessing.Process):
    allLink = set()
    count = 0

    baseUrl = 'https://stackoverflow.com'

    def __init__(self, url, **kwargs):
        super().__init__(**kwargs)
        self.url = url

    def craw(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')

        content = soup.find(id='content')
        for link in content.findAll('a'):
            print(link.text)
            tbl.insert_one({'link': link.text})
            self.count += 1
            print(self.count)
            if 'title' in link.attrs:
                newUrl = self.baseUrl + link.attrs['href']
                if 'go to page' in link.attrs['title'] and newUrl not in self.allLink:
                    self.allLink.add(newUrl)
                    self.craw(newUrl)

    def run(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')

        content = soup.find(id='content')
        for link in content.findAll('a'):
            self.count += 1
            print(link.text)
            print(self.count)
            if 'title' in link.attrs:
                newUrl = self.baseUrl + link.attrs['href']
                self.allLink.add(newUrl)
                if 'go to page' in link.attrs['title'] and newUrl not in self.allLink:
                    self.run()
            else:
                newUrl = self.baseUrl + link.attrs['href']
                self.run()

if __name__ == '__main__':
    url = 'https://stackoverflow.com/questions/tagged/python'
    Crawler(url).craw(url)