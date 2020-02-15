# coding: utf-8
import DBTool
import BeautifulSoupTool

basicUrl = "https://cb.386i.xyz/"
selfPhotoArea = basicUrl + "thread0806.php?fid=16/"
otherPhotoArea = basicUrl + "thread0806.php?fid=8/"


# wholeURL = basicUrl + "htm_data" + /1712/16/2864132.html


# 删除列表中，数据库内已存在的列
def deleteOldURL(nameList: list, urlList: list, tableMame: str):
    dataInDB = DBTool.getNameList(tableMame)
    for (name, nameUrl) in zip(nameList.copy(), urlList.copy()):
        if name in dataInDB:
            nameList.remove(name)
            urlList.remove(nameUrl)
    return nameList, urlList


def update(tpmUrl, tableName):
    stopCount = 0

    try:
        for index in range(100):
            stopCount = index
            url = tpmUrl + "&search=&page=" + str(index + 1)
            names, urls = BeautifulSoupTool.getOnePage(url)
            names, urls = deleteOldURL(names, urls, tableName)
            if len(names) == 0 or len(urls) == 0:
                print("已全部跟新完毕")
                break
            print("==================================================")
            print("第" + str(index + 1) + "页下载完成")
            print("本页更新内容为：")
            print(names)
            print("正在更新数据库...")
            DBTool.insertSQLs(names, urls, tableName)
            print("数据库已更新")
            print("**************************************************")

    except Exception as e:
        print(e)
        print("出现错误")
        print("停止在" + str(stopCount + 1) + "页")
    print("=======================")
    print("全部下载完成")


# 自拍区
def updatePictures():
    update(selfPhotoArea, "pictures")


# 写真区
def updatePhotos():
    update(otherPhotoArea, "photos")

# if __name__ == '__main__':
#
#     # 自拍区
#     # update(selfPhotoArea, "pictures")
#
#     # 写真区
#     update(otherPhotoArea, "photos")
