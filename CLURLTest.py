# coding: utf-8
import requests
from bs4 import BeautifulSoup
import os
import re
import time

Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',

}
path = "C:\\Share\\CLResult\\";
txtPath = "C:\\Github\\CLTxtTest\\"

# basicUrl = "https://cl.bbcb.xyz"
basicUrl = "https://cc.vttg.pw"
startPath = basicUrl + "/thread0806.php?fid=16"

stopCount = 0
maxPage = 1
minPage = 0
nowPage = 0


def getMaxPage():
    maxPagePath = "SaveData.txt"
    file = open(maxPagePath)
    max = file.read()
    file.close()
    return int(max)


def open_URL(url):
    try:
        # req = requests.get(url, headers=Hostreferer, stream=True, timeout=20, proxies=proxies)
        req = requests.get(url, headers=Hostreferer, stream=True, timeout=20)
        req.encoding = "gbk"
        if req.status_code == 200:
            return req
    except Exception as e:
        print("except", e)
        for i in range(1, 10):
            print('请求超时，第%s次重复请求' % i)
            # req = requests.get(url, headers=Hostreferer, stream=True, timeout=20, proxies=proxies)
            req = requests.get(url, headers=Hostreferer, stream=True, timeout=20)
            req.encoding = "gbk"
            if req.status_code == 200:
                return req
        time.sleep(10)
        # req = requests.get(url, headers=Hostreferer, stream=True, timeout=20, proxies=proxies)
        req = requests.get(url, headers=Hostreferer, stream=True, timeout=20)
        req.encoding = "gbk"
        if req.status_code == 200:
            return req


# 获得总页面html代码
def get_html(htmlUrl):
    req = open_URL(htmlUrl)
    html = ""
    try:
        html = req.text
        req.close()
    except Exception as e:
        print("except", e)
        time.sleep(10)
        req = open_URL(htmlUrl)
        html = req.text
    return html


def rename(name):
    rstr = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(rstr, "", name)
    return new_name


def saveTxt(name, datgaList):
    if "\\" in name:
        print(name)
        name = name.replace('\\', '')
    try:
        file = open(txtPath + name, 'w+')
        for oneData in datgaList:
            file.write(oneData.replace(u'\xa0', u'') + "\n")
    except Exception as e:
        print(name)
        print("except", e)


def saveOneAlbumText(url, name):
    new_name = rename(name)
    if new_name+".txt" not in os.listdir(txtPath):
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        imgs = soup.findAll("input", {"type": "image"})
        urlList = []
        print("第" + str(nowPage + 1) + "页")
        print("图集--" + name + "--开始保存")
        for i in range(0, len(imgs)):
            urlList.append(imgs[i].get('data-src'))
        saveTxt(new_name+".txt", urlList)
        print("图集--" + name + "保存成功")
    else:
        print(new_name + "已存在")


def findAllAlbum(url):
    req = open_URL(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    albums = soup.find_all("td", {"class": "tal"})
    urlList = []
    nameList = []
    if nowPage == 0:
        albums = albums[9:-1]
    for album in albums:
        nameList.append(album.h3.a.string)
        urlList.append(basicUrl+"/"+album.h3.a.get('href'))
    return urlList, nameList

def save_one_page(url):

    results = findAllAlbum(url)
    urls = results[0]
    names = results[1]
    for i in range(0, len(urls)):
        saveOneAlbumText(urls[i], names[i])
        time.sleep(0.1)


def saveData():
    file = open("SaveData.txt", 'w+')
    file.write(str(nowPage))


def saveErrorMessage(message):
    file = open("ErrorMessage.txt", 'w+')
    file.write(message)

if __name__ == '__main__':
    try:
        # maxPage = getMaxPage()
        stopCount = maxPage
        for count in range(minPage, maxPage):
            stopCount = count + 1
            nowPage = count
            url = startPath + "&search=&page=" + str(count+1)
            save_one_page(url)
    except Exception as e:
        saveErrorMessage(e)
    finally:
        print("爬取完成")
        print("停止在" + str(stopCount) + "页")
        saveData()
        # os.system("shutdown -s -t 10")

