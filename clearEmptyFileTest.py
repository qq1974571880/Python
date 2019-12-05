import os

# docPath = "C:\\Github\\Python\\ClearEmptyFileTestData\\"
basicPath = "D:\\Share\\CLResult"


def deleteOneFolder(folderPath):
    lists = os.listdir(folderPath)
    for file in lists:
        filePath = folderPath + "\\" + file
        fileSpace = os.path.getsize(filePath)
        if fileSpace == 0:
            print(filePath)
            print(fileSpace)
            print("======")
            os.remove(filePath)

# def checkEmptyFolder(folderPath):
#     lists = os.listdir(folderPath)
#     for file in lists:
#         print(file)



lists = os.listdir(basicPath)
for doc in lists:
    docPath = basicPath + "\\" + doc

    if "." not in docPath:
        deleteOneFolder(docPath)

    # 判断文件夹是否为空
    # if not os.listdir(docPath):
    #     print(doc + "文件夹为空")

        # 删除文件夹
        # os.removedirs(docPath)

        #删除文件
        # os.remove(docPath)

print("删除完成")




