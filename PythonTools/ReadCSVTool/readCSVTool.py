import csv


# 转换前
# [['case', 'xx', 'yy', 'expectedResults', 'comments', 'remarks'],
# ['case1', 'x1', 'y1', 'x1,y1', 'com1', 'rem1'],
# ['case2', 'x2', 'None', 'x2,y2', 'com2', 'rem2']]

# 转换成纵列之后
# { 'case': ['case1', 'case2'],
#   'xx': ['x1', 'x2'],
#   'yy': ['y1', None],
#   'expectedResults': ['x1,y1', 'x2,y2'],
#   'comments': ['com1', 'com2'],
#   'remarks': ['rem1', 'rem2'] }

def csvToList(path):
    csv_reader = csv.reader(open(path, encoding='utf-8'))

    # 转化csv为dictionary, 列的第一项为key，第二项至最后一项为value(list)
    fileData = list(csv_reader)
    resultDict = {}
    noneList = ["None", "none", "Null", "null"]
    falseList = ["False", "false"]
    trueList = ["True", "true"]
    for i in range(0, len(fileData[0])):
        tmpList = []
        for j in range(0, len(fileData)):
            if j != 0:
                if fileData[j][i].strip() in noneList:
                    tmpList.append("")
                elif fileData[j][i].strip() in falseList:
                    tmpList.append(False)
                elif fileData[j][i].strip() in trueList:
                    tmpList.append(True)
                else:
                    tmpList.append(fileData[j][i])
        resultDict[fileData[0][i]] = tmpList
    return resultDict
