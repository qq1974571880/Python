import csv
csv_reader = csv.reader(open('testData.csv', encoding='utf-8'))

# 转化csv为list
fileData = list(csv_reader)
resultList = []
noneList = ["", "None", "none", "Null", "null"]

# 转换前
# [['case', 'xx', 'yy', 'expectedResults', 'comments', 'remarks'],
# ['case1', 'x1', 'y1', 'x1,y1', 'com1', 'rem1'],
# ['case2', 'x2', 'None', 'x2,y2', 'com2', 'rem2']]

# 转换成纵列之后
# [['case', 'case1', 'case2'],
# ['xx', 'x1', 'x2'],
# ['yy', 'y1', None],
# ['expectedResults', 'x1,y1', 'x2,y2'],
# ['comments', 'com1', 'com2'],
# ['remarks', 'rem1', 'rem2']]
for i in range(0, len(fileData[0])):
    tmpList = []
    for j in range(0, len(fileData)):
        if fileData[j][i].strip() in noneList:
            tmpList.append(None)
        else:
            tmpList.append(fileData[j][i])
    resultList.append(tmpList)
print(resultList)
