# coding: utf-8
import requests
from bs4 import BeautifulSoup
import os
import re
import time
import datetime

Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',

}

localBasicPath = "C:\\Github\\CLTxtTest\\"
txtPath = "C:\\Github\\CLTxtTest\\"

basicUrl = "https://cb.wpio.xyz"
startPath = basicUrl + "/thread0806.php?fid=16"

stopCount = 0
maxPage = 20
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
        req = requests.get(url, headers=Hostreferer, stream=True, timeout=30)
        req.encoding = "gbk"
        if req.status_code == 200:
            return req
    except Exception as e:
        print("except", e)
    #     for i in range(1, 10):
    #         print('请求超时，第%s次重复请求' % i)
    #         # req = requests.get(url, headers=Hostreferer, stream=True, timeout=20, proxies=proxies)
    #         req = requests.get(url, headers=Hostreferer, stream=True, timeout=30)
    #         req.encoding = "gbk"
    #         if req.status_code == 200:
    #             return req
        time.sleep(50)
    #     # req = requests.get(url, headers=Hostreferer, stream=True, timeout=20, proxies=proxies)
        req = requests.get(url, headers=Hostreferer, stream=True, timeout=30)
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


def saveOneAlbumText(url, name, compareList):
    new_name = rename(name)
    # os.listdir(txtPath):
    if new_name+".txt" not in compareList:
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        # imgs = soup.findAll("input", {"type": "image"})
        imgs = soup.findAll("img")
        urlList = []
        print("第" + str(nowPage + 1) + "页")
        print("图集--" + name + "--开始保存")
        for i in range(0, len(imgs)):
            urlList.append(imgs[i].get('data-src'))
        saveTxt(new_name+".txt", urlList)
        print("图集--" + name + "保存成功")
        return 0
    else:
        print(new_name + "已存在")
        return 1


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

def save_one_page(url, compareList):

    results = findAllAlbum(url)
    urls = results[0]
    names = results[1]
    allURLLists = 0
    for i in range(0, len(urls)):
        allURLLists += saveOneAlbumText(urls[i], names[i], compareList)
        time.sleep(0.1)
    print("====================")
    print(allURLLists)
    print(len(urls))
    print("====================")
    if allURLLists == len(urls):
        print("已下载到完结页")
        return True
    else:
        return False

def saveData():
    file = open("SaveData.txt", 'w+')
    file.write(str(nowPage))


def canCreateNewFolder(path):
    if str(datetime.date.today()) not in os.listdir(path):
        return True
    else:
        return False


def getAllFileFromOneFolder(path):
    fileList = os.listdir(path)
    return fileList


def getAllfile(path):
    folderList = os.listdir(path)
    compareList = []
    for folderName in folderList:
        fileList = getAllFileFromOneFolder(localBasicPath + folderName)
        compareList += fileList
    return compareList


if __name__ == '__main__':
    compareList = getAllfile(localBasicPath)
    if canCreateNewFolder(txtPath):
        txtPath += str(datetime.date.today()) + "\\"
        os.mkdir(txtPath)
        try:
            stopCount = maxPage
            for count in range(minPage, maxPage):
                stopCount = count + 1
                nowPage = count
                url = startPath + "&search=&page=" + str(count + 1)
                if save_one_page(url, compareList):
                    break
        except Exception as e:
            print("爬取完成")
            print("停止在" + str(stopCount) + "页")
            # saveData()
            # os.system("shutdown -s -t 10")
        print("下载完成")
    else:
        print(str(datetime.date.today()) + "文件夹已存在")


