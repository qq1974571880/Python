# coding: utf-8
import DBTool
import os
import shutil


bathPath = "D:\\Share\\CLResult\\"
selfPhotosPath = "D:\\CLPictures\\自拍\\"


# 获取路径下的列名
def getPathNameList(path) -> list:
    return os.listdir(path)


def moveFolder(oldPath, newPath):
    shutil.move(oldPath, newPath)


def findAndMove():
    dbNameList = DBTool.getNameList()
    pathNameList = getPathNameList(bathPath)
    resultNameList = []
    for name in dbNameList:
        if name in pathNameList:
            shutil.move(bathPath + name, selfPhotosPath)
            resultNameList.append(name)
    return True


def updateDB():
    try:
        names = getPathNameList(selfPhotosPath)
        DBTool.updateSQLs(names)
        print("更新成功")
    except Exception as e:
        print("出现错误，错误情况为：")
        print(e)


if __name__ == '__main__':
    # if findAndMove():
    #     print("移动成功")
    # else:
    #     print("移动失败")
    updateDB()
