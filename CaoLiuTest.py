# coding:gbk
import requests
from bs4 import BeautifulSoup
import os
import re
import time

Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}
Picreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

path = "C:\\Share\\CLResult\\";
txtPath = "C:\\Github\\CLTxtTest\\"

basicUrl = "https://cl.bbcb.xyz"
startPath = basicUrl + "/thread0806.php?fid=16"

stopCount = 0
maxPage = 88
minPage = 0
nowPage = 0


def open_URL(url):
    try:
        req = requests.get(url, headers=Hostreferer, stream=True,timeout=20)
        req.encoding = "gbk"
        if req.status_code == 200:
            return req
    except Exception as e:
        print("except",e)
        for i in range(1, 10):
            print('锟斤拷锟斤拷时锟斤拷锟斤拷%s锟斤拷锟截革拷锟斤拷锟斤拷' % i)
            req = requests.get(url, headers=Hostreferer, stream=True, timeout=20)
            req.encoding = "gbk"
            if req.status_code == 200:
                return req
        time.sleep(10)
        req = requests.get(url, headers=Hostreferer, stream=True, timeout=20)
        req.encoding = "gbk"
        if req.status_code == 200:
            return req



def get_html(htmlUrl):  # 锟斤拷锟斤拷锟揭筹拷锟絟tml锟斤拷锟斤拷
    req = open_URL(htmlUrl)
    html = ""
    try:
        html = req.text
    except Exception as e:
        print("except", e)
        time.sleep(10)
        req = open_URL(htmlUrl)
        html = req.text
    return html


# 锟斤拷锟芥单锟斤拷图片

def save_img(img_url, count, name):
    req = open_URL(img_url)
    new_name = rename(name)
    print()
    name = ".jpg"
    if ".gif" in img_url:
        return
    with open(path+new_name + '/' + str(count) + name, 'wb') as f:
        f.write(req.content)

def rename(name):
    rstr = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(rstr, "", name)
    return new_name


def saveTxt(name, datgaList):
    if "\\" in name:
        print(name)
        name = name.replace('\\', '')
    file = open(txtPath + name, 'w+')
    for oneData in datgaList:
        file.write(oneData.replace(u'\xa0', u'') + "\n")


def saveOneAlbumText(url, name):
    new_name = rename(name)
    if new_name+".txt" not in os.listdir(txtPath):
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        imgs = soup.findAll("input", {"type": "image"})
        urlList = []
        print("锟斤拷" + str(nowPage + 1) + "页")
        print("图锟斤拷--" + name + "--锟斤拷始锟斤拷锟斤拷")
        for i in range(0, len(imgs)):
            urlList.append(imgs[i].get('data-src'))
        saveTxt(new_name+".txt", urlList)
        print("图锟斤拷--" + name + "锟斤拷锟斤拷晒锟?")
    else:
        print(new_name + "锟窖达拷锟斤拷")


def saveOneAlbum(url,name):
    new_name = rename(name)
    if new_name not in os.listdir(path):
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        print(url)
        os.mkdir(path + new_name)
        print("锟斤拷" + str(nowPage +1) + "页")
        print("图锟斤拷--" + name + "--锟斤拷始锟斤拷锟斤拷")
        imgs = soup.findAll("input",{"type":"image"})
        for i in range(0,len(imgs)):
            try:
                save_img(imgs[i].get('data-src'), i + 1, name)
                print('锟斤拷锟节憋拷锟斤拷锟?' + str(i + 1) + '锟斤拷图片')
            except Exception as e:
                print("except",e)
                continue
        print("图锟斤拷--" + name + "锟斤拷锟斤拷晒锟?")
    else:
        print(new_name + "锟窖达拷锟斤拷")


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
        # saveOneAlbum(urls[i],names[i])
        saveOneAlbumText(urls[i],names[i])

if __name__ == '__main__':
    try:
        # for count in range(minPage, maxPage):
        for count in range(maxPage,minPage,-1):
            stopCount = count + 1
            nowPage = count
            url = startPath + "&search=&page=" + str(count+1)
            save_one_page(url)

    finally:
        print("锟斤拷取锟斤拷锟?")
        print("停止锟斤拷" + str(stopCount) + "页")
        # os.system("shutdown -s -t 10")

