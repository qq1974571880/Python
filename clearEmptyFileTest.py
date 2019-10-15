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



lists = os.listdir(basicPath)
for doc in lists:
    docPath = basicPath + "\\" + doc
    if "." not in docPath:
        deleteOneFolder(docPath)
print("删除完成")




