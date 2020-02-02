# coding: utf-8
import DBTool
import BeautifulSoupTool

basicUrl = "https://cb.386i.xyz/"
selfPhotoArea = basicUrl + "thread0806.php?fid=16"
otherPhotoArea = basicUrl + "thread0806.php?fid=8"

# wholeURL = basicUrl + "htm_data" + /1712/16/2864132.html


def download(tpmUrl, tableName):
    stopCount = 0
    try:
        for index in range(90, 0, -1):
            stopCount = index
            url = tpmUrl + "&search=&page=" + str(index + 1)
            names, urls = BeautifulSoupTool.getOnePage(url)
            DBTool.insertSQLs(names, urls, tableName)
            print("第" + str(index + 1) + "页下载完成")

    except Exception as e:
        print(e)
        print("出现错误")
        print("停止在" + str(stopCount + 1) + "页")
    print("=======================")
    print("全部下载完成")


if __name__ == '__main__':

    # 自拍区
    download(selfPhotoArea, "pictures")

    # 写真区
    # download(otherPhotoArea, "photos")
