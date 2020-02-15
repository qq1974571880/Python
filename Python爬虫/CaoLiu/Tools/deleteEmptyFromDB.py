import DBTool
import os


def clear(path:str):
    count = 0
    files = os.listdir(path)
    for file in files:
        if ".txt" in file and os.path.getsize(path + file) == 0:
            os.remove(path + file)
            count += 1
    print("一共删除了" + str(count) + "个文件")


def getEmptyFiles(path):
    result = []
    files = os.listdir(path)
    for file in files:
        if ".txt" in file and os.path.getsize(path + file) == 0:
            result.append(file[0:-4])
    return result


def deletePictures():
    print("开始删除")
    DBTool.deleteDBByName("pictures", getEmptyFiles("D:\\CL\\tmpDownloadTxt\\"))
    print("数据库内已删除")
    clear("D:\\CL\\tmpDownloadTxt\\")
    print("文件已删除，删除结束")


def deletePhotos():
    print("开始删除")
    DBTool.deleteDBByName("photos", getEmptyFiles("D:\\CL\\tmpDownloadTxt\\"))
    print("数据库内已删除")
    clear("D:\\CL\\tmpDownloadTxt\\")
    print("文件已删除，删除结束")
