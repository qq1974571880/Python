import multiprocessing
import DBTool
import BeautifulSoupTool
import CommonResource


def saveTxt(name: str, dataList: list):
    name = CommonResource.rename(name)
    try:
        file = open(file=CommonResource.tmpDownloadTxt + name + ".txt", mode='w+')
        for oneData in dataList:
            file.write(oneData.replace(u'\xa0', u'') + "\n")
        file.close()
    except Exception as e:
        print(name)
        print("except", e)


def downloadOne(name: str, url: str):
    pics = BeautifulSoupTool.getURLListFromURL(url)
    if len(pics) > 0:
        saveTxt(name, pics)
    else:
        print(name + "没有url")


def downloadAll(tableName: str):

    # 从数据库读取待下载的name以及url
    results = DBTool.getNameListByTxt(tableName)
    names = []
    urls = []
    for result in results:
        names.append(result[0])
        urls.append(result[1])
    print("共" + str(len(names)) + "个")
    pool = multiprocessing.Pool(processes=50)
    print("正在加入进程池")
    for i in range(0, len(names)):
        pool.apply_async(downloadOne, (names[i], urls[i]))
    pool.close()
    pool.join()
    print("下载完毕")


def downloadPicturesTxt():
    downloadAll("pictures")


def downloadPhotosTxt():
    downloadAll("photos")
