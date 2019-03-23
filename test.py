from urllib import  request
from bs4 import BeautifulSoup

url = 'http://127.0.0.1/test.html'
headers = {'User-Agent':'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read()
page_info = page_info.decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')
titles = soup.find_all('div', '111')
for title in titles:
    print(title)
