# coding: utf-8
import DBTool
import BeautifulSoupTool

basicUrl = "https://cb.386i.xyz/"
selfPhotoArea = basicUrl + "thread0806.php?fid=16/"
otherPhotoArea = basicUrl + "thread0806.php?fid=8/"

# wholeURL = basicUrl + "htm_data" + /1712/16/2864132.html

stopCount = 0


# 删除列表中，数据库内已存在的列
def deleteOldURL(nameList: list, urlList: list):
    dataInDB = DBTool.getNameList()
    for (name, nameUrl) in zip(nameList.copy(), urlList.copy()):
        if name in dataInDB:
            nameList.remove(name)
            urlList.remove(nameUrl)
    return nameList, urlList


if __name__ == '__main__':
    try:
        for index in range(100):
            stopCount = index
            url = selfPhotoArea + "&search=&page=" + str(index + 1)
            names, urls = BeautifulSoupTool.getOnePage(url)
            names, urls = deleteOldURL(names, urls)
            if len(names) == 0 or len(urls) == 0:
                print("已全部跟新完毕")
                break
            DBTool.insertSQLs(names, urls)
            print("本页更新内容为：")
            print(names)
            print("第" + str(index + 1) + "页下载完成")

    except Exception as e:
        print(e)
        print("出现错误")
        print("停止在" + str(stopCount + 1) + "页")
    print("=======================")
    print("全部下载完成")