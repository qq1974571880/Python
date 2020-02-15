import os
import DBTool

# 设计用来匹配本地图片和DB

pathList = DBTool.getNameListFromFolder()

basePhotoPath = "D:\\CL\\CLPictures\\写真\\"
basePicturePath = "D:\\CL\\CLPictures\\自拍\\"


def getNameList(path: str) -> list:
    return os.listdir(path)


for path in pathList:
    print(getNameList(basePicturePath + path.replace("\\\\", "\\")))
