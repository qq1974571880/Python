import os
import shutil

import DBTool

oldPicPath = "D:\\CL\\tmpDownloadPic\\"
oldTxtPath = "D:\\CL\\tmpDownloadTxt\\"
photoPath = "D:\\CL\\CLPictures\\写真\\"
picturePath = "D:\\CL\\CLPictures\\自拍\\"
photoTxtPath = "D:\\CL\\CLTXT\\写真\\"
pictureTxtPath = "D:\\CL\\CLTXT\\自拍\\"


def moveFolders(tableName: str, oldPath: str, path: str, line: str):
    folders = os.listdir(oldPath)
    print(folders)
    print("开始执行")
    while len(folders) > 0:
        #
        # 获取能存的文件夹路径
        result = DBTool.getMinPathFromFolder(tableName)
        dbNum = int(result[1])
        dbID = result[2]

        # 获取能存的数量
        num = 1000 - dbNum

        # 存放指定数量
        if num < len(folders):
            tmpList = folders[0:num]
            dbNum = 1000
            folders = folders.copy()[num:-1]
        #
        else:
            tmpList = folders.copy()
            folders = []
            dbNum += len(tmpList)
        print("开始移动文件，共" + str(len(tmpList)) + "个")
        print("移动至：" + path + result[0])
        # 挪文件夹或文件
        for folderName in tmpList:
            if os.path.exists(path + result[0]) is False:
                shutil.move(oldPath + folderName, path + result[0])
            else:
                print(result[0] + "  文件已存在，移动失败")

        print("开始更新数据库")

        # # 更新数据库
        resultList = []
        if line == "txtPath":
            for tmp in tmpList.copy():
                resultList.append(tmp[0:-4])
            tmpList = resultList

        if tableName == "folders" or tableName == "txtFolders":
            DBTool.updatePicPathFromPictures(result[0], tmpList, "pictures", line)
        else:
            DBTool.updatePicPathFromPictures(result[0], tmpList, "photos", line)
        DBTool.updateNumFromFolder(dbNum, dbID, tableName)

    print("全部移动完毕")


def choose(param1: str, param2: str):
    if param1 == "图片":
        if param2 == "自拍":
            moveFolders("folders", oldPicPath, picturePath, "picPath")
        else:
            moveFolders("photosFolders", oldPicPath, photoPath, "picPath")
    else:
        if param2 == "自拍":
            moveFolders("txtFolders", oldTxtPath, pictureTxtPath, "txtPath")
        else:
            moveFolders("photosTxtFolders", oldTxtPath, photoTxtPath, "txtPath")


if __name__ == '__main__':
    choose("文字", "自拍")
    # moveFolders(picturePath)
    # moveFolders(photoPath)
