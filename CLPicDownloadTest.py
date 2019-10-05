import requests
import os
import re
import time
import datetime
import multiprocessing

Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/77.0.3865.90 Safari/537.36',
}

picPath = "D:\\Share\\CLResult"
txtPath = "C:\\Github\\CLTxtTest\\" + str(datetime.date.today())

nowPicCount = 0

urlList = []

def open_url(url):
    # try:
    requests.adapters.DEFAULT_RETRIES = 5
    req = requests.get(url, headers=Hostreferer, stream=True, timeout=30)
    return req
    # except Exception as e:
    #     print("open_urlError:", e)

# 保存单张图片
def save_img(img_url, count, path):
    if "gif" in img_url:
        return
    req = open_url(img_url)
    print(path + "正在保存" + str(count))
    # print("保存进度" + str(count) )
    with open(path + '/' + str(count) + '.jpg', 'wb') as f:
        # try:
        f.write(req.content)
        req.close()
        time.sleep(0.5)
        # except Exception as e:
        #     print("save_imgError:" + e)


def saveAlbum(name, picList):
    # 1.判断地址有无同名文件夹
    if name not in os.listdir(picPath):
        # 2.创建文件夹
        os.mkdir(picPath + "\\" + name)
        # 3.针对list调用保存单张图片
        picNum = len(picList)

        albumList = []
        for i in range(0, picNum):
            # try:
                albumList.append([picList[i], i+1, picPath + "\\" + name])
                # print("保存进度" + str(i + 1) + "/" + str(picNum))
                # save_img(picList[i], i + 1, picPath + "\\" + name)
            # except Exception as e:
            #     continue
        urlList.append(albumList)
    else:
        print("文件已存在")


def rename(name):
    rstr = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(rstr, "", name)
    return new_name


def getURLLists(path):
    lines = []
    with open(path, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines

def saveData():
    file = open("SaveData.txt", 'w+')
    file.write(str(nowPicCount))


if __name__ == '__main__':
    txtLists = os.listdir(txtPath)
    num = len(txtLists)
    try:
        for i in range(0, num):
            nowPicCount = i
            print("-------------------------------")
            print("正在保存第 " + str(i+1) + "组图片" + "——————" + txtLists[i])
            folderName = txtLists[i].split(".txt")[0]
            lines = getURLLists(txtPath + "\\" + txtLists[i])
            saveAlbum(folderName, lines)
            print("-------------------------------")

        pool = multiprocessing.Pool(processes=100)
        for i in range(0,len(urlList)):
            for j in range(0,len(urlList[i])):
                pool.apply_async(save_img, (urlList[i][j][0], urlList[i][j][1], urlList[i][j][2]))
        pool.close()
        pool.join()
        print("下载完毕")
    except Exception as e:
        saveData()
        print("mainError:" + e)
        print("发生错误")

