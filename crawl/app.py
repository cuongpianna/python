import requests
from bs4 import BeautifulSoup
import csv
import multiprocessing
import pymongo

from pymongo import MongoClient
client = MongoClient()
db = client['hihi']
tbl = db['artist']

# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
#
# soup = BeautifulSoup(page.text,'html.parser')
#
# artist_name_list = soup.find(class_='BodyText')
#
# f = csv.writer(open('test.csv','w'))
# f.writerow(['Name'])
#
# # Pull text from all instances of <a> tag within BodyText div
# artist_name_list_items = artist_name_list.find_all('a')
# for artist_name in artist_name_list_items:
#     print(artist_name.contents[0])
#     f.writerow([artist_name.contents[0]])

def craw(page):
    soup = BeautifulSoup(page.text,'html.parser')
    artist_name_list = soup.find(class_='BodyText')

    artist_list = artist_name_list.find_all('a')
    lena = ['s','c','i']
    for item in lena:
        print(item)
        tbl.insert_one({'name':item})

if __name__ == '__main__':
    page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    craw(page)
    p1 = multiprocessing.Process(target=craw,args=(page,))
    p1.start()
    p1.join()
    #tbl.insert_one('s')

