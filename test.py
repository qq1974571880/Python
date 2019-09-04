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

path = "C:\\Github\\91Result\\";

def get_page_name(url):  # 获得图集最大页数和名称
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    span = soup.findAll('span')
    title = soup.find('h2', class_="main-title")
    return span[9].text, title.text


def get_html(url):  # 获得页面html代码
    req = requests.get(url, headers=Hostreferer)
    html = req.text
    return html


def get_img_url(url, name):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    img_url = soup.find('img', alt=name)
    return img_url['src']


def save_img(img_url, count, name):
    req = requests.get(img_url, headers=Picreferer)
    print(img_url)
    new_name = rename(name)
    with open(path+new_name + '/' + str(count) + '.jpg', 'wb') as f:
        f.write(req.content)


def rename(name):
    rstr = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(rstr, "", name)
    return new_name


# 保存一个图片集内的所有图片
def save_one_atlas(old_url):
    page, name = get_page_name(old_url)
    new_name = rename(name)
    os.mkdir(path+new_name)
    print("图集--" + name + "--开始保存")

    # 保存每张图片
    for i in range(1, int(page) + 1):
        url = old_url + "/" + str(i)
        img_url = get_img_url(url, name)
        save_img(img_url, i, name)
        print('正在保存第' + str(i) + '张图片')
    print("图集--" + name + "保存成功")


def get_atlas_list(url):
    req = requests.get(url, headers=Hostreferer)
    soup = BeautifulSoup(req.text, 'html.parser')
    atlas = soup.find_all(attrs={'class': 'lazy'})
    atlas_list = []
    for atla in atlas:
        print(atla)
        atlas_list.append(atla.parent['href'])
    return atlas_list


# 保存单页的所有图片集的url 例如 https://www.mzitu.com/173911
def save_one_page(start_url):
    atlas_url = get_atlas_list(start_url)
    for url in atlas_url:
        save_one_atlas(url)


if __name__ == '__main__':
    start_url = "https://www.mzitu.com/"
    for count in range(1, 3):
        url = start_url + "page/" + str(count) + "/"
        save_one_page(url)
    print("爬取完成")