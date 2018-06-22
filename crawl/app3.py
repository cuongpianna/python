import csv
import requests
import multiprocessing
import pymongo
from bs4 import BeautifulSoup

f = csv.writer(open('stack.csv','w'))
f.writerow(['title','question'])

class Crawler(multiprocessing.Process):
    pages = set()
    count = 0

    baseUrl = 'https://stackoverflow.com'

    def __init__(self,url,**kwargs):
        super().__init__(**kwargs)
        self.url = url

    def crawler(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')

        content = soup.find(id='content')

        for link in content.findAll('a'):
            self.count += 1
            if 'class' in link.attrs:
                if 'question-hyperlink' in link.attrs['class']:
                    if 'https' not in link.attrs['href']:
                        print(self.get_title(self.baseUrl+link.attrs['href']))
                        print('QUESTION BODY: {}'.format(self.get_body_question(self.baseUrl+link.attrs['href'])))
                        f.writerow([self.get_title(self.baseUrl+link.attrs['href']),self.get_body_question(self.baseUrl+link.attrs['href'])])

            elif 'title' in link.attrs:
                if 'go to page' in link.attrs['title']:
                    print('-------------------')
                    if link.attrs['href'] not in self.pages:
                        self.pages.add(link.attrs['href'])
                        print(link.attrs['href'])
                        self.crawler(self.baseUrl+link.attrs['href'])




    def get_title(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        title = soup.find(class_='question-hyperlink')
        if title:
            return title.text
        else:
            return ''

    def get_body_question(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        body = soup.find(id='question')
        text = body.find(class_='post-text')
        if text:
            return text.text
        else:
            return 'no body'



if __name__ == '__main__':
    url = 'https://stackoverflow.com/questions/tagged/python'
    url2 = 'https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance'
    Crawler(url).crawler(url)
