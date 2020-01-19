# coding: utf-8
import requests
from bs4 import BeautifulSoup
import time

Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

basicUrl = "https://cb.386i.xyz/"
selfPhotoArea = basicUrl + "thread0806.php?fid=16/"
otherPhotoArea = basicUrl + "thread0806.php?fid=8/"

# wholeURL = basicUrl + "htm_data" + /1712/16/2864132.html

stopCount = 0


def open_URL(htmlURL):
    try:
        req = requests.get(htmlURL, headers=Hostreferer, stream=True, timeout=30)
        req.encoding = "gbk"
        if req.status_code == 200:
            return req
    except Exception as e:
        print("except", e)
        time.sleep(50)
        req = requests.get(htmlURL, headers=Hostreferer, stream=True, timeout=30)
        req.encoding = "gbk"
        if req.status_code == 200:
            return req


# 获得总页面html代码
def get_html(htmlUrl):
    req = open_URL(htmlUrl)
    try:
        htmlStr = req.text
        req.close()
    except Exception as e:
        print("except", e)
        time.sleep(30)
        req = open_URL(htmlUrl)
        htmlStr = req.text
    return htmlStr


def getOnePage(htmlUrl):
    html = get_html(htmlUrl)
    soup = BeautifulSoup(html, 'html.parser')
    albums = soup.find_all("td", {"class": "tal"})
    urlList = []
    nameList = []
    if "page=1" in htmlUrl:
        albums = albums[9:-1]
    for album in albums:
        wholeName = album.h3.a.string
        nameList.append(wholeName)
        wholeURL = album.h3.a.get('href')
        urlList.append(wholeURL.split("htm_data")[1])
    return nameList, urlList