import xlrd
import pandas as pd
import os
import shutil


def getExcelDataToList(excelPath) -> list:

    # 读取Excel
    wb = xlrd.open_workbook(excelPath)

    # 获取所有的sheet名称
    sheet_names = wb.sheet_names()

    # 创建结果集
    resultList = []
    for index in range(0, len(sheet_names)):

        # 清洗数据 and 存放list
        ws = wb.sheet_by_name(sheet_names[index])

        rowNum = ws.nrows
        colNum = ws.ncols

        sheetDict = {}
        for col in range(0, colNum):
            colList = []
            for row in range(0, rowNum):
                c_type = ws.cell(row, col).ctype
                c_cell = ws.cell_value(row, col)

                if c_type == 1 and c_cell.strip() in ["None", "none", "Null", "null", ""]:
                    c_cell = "None"

                # 如果是整形
                elif c_type == 2 and c_cell % 1 == 0:
                    c_cell = int(c_cell)
                elif c_type == 3:

                    # 转成datetime对象
                    date = xlrd.xldate.xldate_as_datetime(ws.cell(row, col).value, 0)
                    c_cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif c_type == 4:
                    c_cell = True if c_cell == 1 else False

                colList.append(c_cell)
            sheetDict[colList[0]] = colList[1:]
        resultList.append({"data": sheetDict, "sheetName": sheet_names[index]})
    return resultList


# 先判断是否有该文件夹,有的话就删除
# 创建文件夹
def createFolder(folder_Path):
    if os.path.exists(folder_Path):
        shutil.rmtree(folder_Path)
    os.mkdir(folder_Path)


# 依据sheet名创建CSV文件
def createCSV(resultList):
    for dic in resultList:
        sheetName = dic["sheetName"]
        dataFrame = pd.DataFrame(dic["data"])
        dataFrame.to_csv(folderPath + sheetName + ".csv", index=False, sep=',')
    print("生成成功:")
    print("生成路径为：" + os.getcwd() + "/" + folderPath)
    print("生成文件" + str(len(resultList)) + "个")


if __name__ == "__main__":
    basePath = "source/"
    csvName = "test"
    extensions = ".xlsx"
    folderPath = basePath + csvName + "/"
    createFolder(folderPath)
    csvList = getExcelDataToList(basePath + csvName + extensions)
    createCSV(csvList)


