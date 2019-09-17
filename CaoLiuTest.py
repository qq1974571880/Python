import requests
from bs4 import BeautifulSoup
import os
import re

Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mzitu.com'
}
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://i.meizitu.net'
}

path = "C:\\Share\\CLResult\\";

basicUrl = "https://cl.bbcb.xyz"
startPath = basicUrl + "/thread0806.php?fid=16"

stopCount = 0
maxPage = 100

def get_html(url):  # 获得总页面html代码
    req = requests.get(url, headers=Hostreferer)
    html = req.text
    return html

#保存单张图片
def save_img(img_url, count, name):
    req = requests.get(img_url, headers=Picreferer)
    new_name = rename(name)
    print()
    with open(path+new_name + '/' + str(count) + '.jpg', 'wb') as f:
        f.write(req.content)

def rename(name):
    rstr = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(rstr, "", name)
    return new_name

def saveOneAlbum(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    print(url)
    name = soup.find('h1', class_="title").get_text()
    imgs = soup.findAll('img')
    new_name = rename(name)
    if new_name not in os.listdir(path):
        os.mkdir(path + new_name)
        print("图集--" + name + "--开始保存")
        # 保存每张图片
        for i in range(0, len(imgs)):
            imgUrl = imgs[i].get('src')
            if "http" in imgUrl or "https" in imgUrl:
                save_img(imgs[i].get('src'), i + 1, name)
            else:
                save_img("http:" + imgs[i].get('src'), i + 1, name)
            print('正在保存第' + str(i + 1) + '张图片')
        print("图集--" + name + "保存成功")
    else:
        print(new_name + "已存在")


def findAllAlbum(url):
    req = requests.get(url, headers=Hostreferer)
    soup = BeautifulSoup(req.text, 'html.parser')
    albums = soup.find_all(attrs={'class': 'text-mr-1'})
    list = []
    for album in albums:
        list.append(basicUrl + album.contents[1]["href"])
    return list

def save_one_page(url):
    urls = findAllAlbum(url)
    for oneUrl in urls:
        saveOneAlbum(oneUrl)


if __name__ == '__main__':
    try:
        for count in range(0, maxPage):
            stopCount = count + 1
            print("当前爬取到" + str(count+1) + "页")
            url = startPath + "&search=&page=" + str(count+1)
            print(url)
            save_one_page(url)

    finally:
        print("爬取完成")
        print("停止在" + stopCount + "页")
        # os.system("shutdown -s -t 10")

