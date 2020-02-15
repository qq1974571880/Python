# coding: utf-8
import requests
from bs4 import BeautifulSoup
import time
import CommonResource
import re

Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

basicUrl = "https://cb.386i.xyz/"
selfPhotoArea = basicUrl + "thread0806.php?fid=16/"
otherPhotoArea = basicUrl + "thread0806.php?fid=8/"

# wholeURL = basicUrl + "htm_data" + /1712/16/2864132.html

stopCount = 0


# 访问html文件
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


# 获取当前页面的所有标题以及对应网址
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
        wholeName = CommonResource.rename(wholeName)
        nameList.append(wholeName)
        wholeURL = album.h3.a.get('href')
        if ".html" in wholeURL:
            urlList.append(wholeURL.split("htm_data")[1])
        else:
            urlList.append(wholeURL)
    return nameList, urlList


# 获取指定网址的全部图片
def getURLListFromURL(url) -> list:
    result = []
    html = get_html(basicUrl + "htm_data" + url)
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.findAll("img")
    for i in range(0, len(imgs)):
        if imgs[i].get('data-src') is not None:
            result.append(imgs[i].get('data-src'))
    if len(result) == 0:
        imgs = soup.findAll("input")
        for i in range(0, len(imgs)):
            if imgs[i].get('data-src') is not None:
                result.append(imgs[i].get('data-src'))
    return result


# 保存单张图片
def save_img(img_url, picName, path):
    if "gif" in img_url:
        return
    req = open_URL(img_url)
    with open(path + '/' + picName + '.jpg', 'wb') as f:
        f.write(req.content)
        req.close()
        time.sleep(0.5)
