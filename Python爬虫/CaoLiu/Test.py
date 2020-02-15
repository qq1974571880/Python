import os
import DBTool
import CommonResource


def findIfExit(name: str, url):
    path = CommonResource.pictureTxtPath + url + name + ".txt"
    if os.path.exists(path):
        return True
    else:
        print(name)
        return False


def getSourceFromDB():
    dbSource = DBTool.getDownloadPicInfo("pictures")
    nameList = dbSource[0]
    pathList = dbSource[1]
    idList = dbSource[2]
    result = []
    for i in range(len(nameList)):
        if not findIfExit(nameList[i], pathList[i]):
            result.append([nameList[i], pathList[i]])
    # print(len(result))
    # return result


def test():
    name = "[原创][cl分享团出品][会员投稿]只怪模特太年起，还是我定力不够深！射淫师和MOD的那些事[31P]"

    path = "0\\0\\0\\0\\"
    return findIfExit(CommonResource.rename(name), path)


getSourceFromDB()
