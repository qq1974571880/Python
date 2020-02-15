import DBTool
import re
import multiprocessing
import BeautifulSoupTool
import os


def rename(name):
    replaceString = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(replaceString, "", name).replace(u'\xa0', u' ').replace('【', '[').replace('】', ']')\
        .replace('\x08','')
    return new_name


def openTxt(path):
    lines = []
    with open(path, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines


def getURLByPath(tableName, path, name):
    bathPath = "D:\\CL\\CLTXT\\"
    if tableName == "pictures":
        bathPath += "自拍\\"
    else:
        bathPath += "写真\\"
    bathPath += path + name + ".txt"
    return openTxt(bathPath)


# 在临时路径创建对应文件夹
def createFolders(nameList):
    bathPath = "D:\\CL\\tmpDownloadPic\\"
    for name in nameList:
        if name not in os.listdir(bathPath):
            os.mkdir(bathPath + "\\" + name)


def downloadPic(path:str, img_url:str, picName:str):
    # ['D:\\CL\\tmpDownloadPic\\[賣給女朋友的情趣禮物說要傳給我來艸[20P]', 'http://www.69img.com/u/20171228/13152372.jpg', 0]
    BeautifulSoupTool.save_img(path=path, img_url=img_url, picName=picName)


def getDownloadList(files: list):
    bathPath = "D:\\CL\\tmpDownloadPic\\"

    # 更正图片名字（0.1.2.3）
    downloadList = []
    for file in files:
        urlLists = file[1]

        # 更正图片名字（0.1.2.3）
        for index, url in enumerate(urlLists):
            downloadList.append([bathPath + file[0], url, index])
    return downloadList


def downloadAll(tableName):

    # 从DB里获取待下载的列表（name + path）
    result = DBTool.getDownloadPicInfo(tableName)
    nameList = result[0]
    pathList = result[1]
    files = []

    createFolders(nameList)
    # 读txt获取url
    for i in range(len(nameList)):
        files.append([nameList[i], getURLByPath(tableName, pathList[i], nameList[i])])

    downloadList = getDownloadList(files)
    print("共" + str(len(nameList)) + "个")
    pool = multiprocessing.Pool(processes=50)
    print("正在加入进程池")
    for i in range(0, len(nameList)):
        pool.apply_async(downloadPic, (downloadList[i][0], downloadList[i][1], downloadList[i][2]))
    pool.close()
    pool.join()
    print("下载完毕")




def downloadPictures():
    downloadAll("pictures")


def downloadPhotos():
    downloadAll("photos")


if __name__ == '__main__':
    downloadPictures()