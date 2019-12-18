import xlrd
import pandas as pd
import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


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
def createCSV(resultList, folderPath):
    for dic in resultList:
        sheetName = dic["sheetName"]
        dataFrame = pd.DataFrame(dic["data"])
        dataFrame.to_csv(folderPath + sheetName + ".csv", index=False, sep=',')
    return {"result": True, "info": ["生成成功: ", "生成路径为：" + folderPath, "生成文件" + str(len(resultList)) + "个"]}


def runProject(inPutPath, outPutPath):
    folderName = inPutPath.split("/")[-1].split(".")[0]
    outPutPath = outPutPath + "/" + folderName + "/"
    createFolder(outPutPath)
    csvList = getExcelDataToList(inPutPath)
    result = createCSV(csvList, outPutPath)
    return result


def selectPath(method):
    if method == "input":
        path_ = filedialog.askopenfilename()
        inputPath.set(path_)
    if method == "output":
        path_ = filedialog.askdirectory()
        outputPath.set(path_)


def changeExcelToCSV(entryValue, entry1Value2):
    result = runProject(entryValue, entry1Value2)
    if result["result"]:
        resultList = result["info"]
        messagebox.showinfo(title=resultList[0], message=resultList[1] + "\n" + resultList[2])


root = Tk()
# 得到屏幕宽度
sw = root.winfo_screenwidth()
# 得到屏幕高度
sh = root.winfo_screenheight()

ww = 500
wh = 200

x = (sw-ww) / 2
y = (sh-wh) / 2

root.geometry("%dx%d+%d+%d" %(ww, wh, x, y))


inputPath = StringVar()
outputPath = StringVar()

label1 = Label(root, text="文件路径:")
entry1 = Entry(root, textvariable=inputPath)

button1 = Button(root, text="路径选择", command=lambda: selectPath("input"))
label2 = Label(root, text="输出路径:")
entry2 = Entry(root, textvariable=outputPath)
button2 = Button(root, text="路径选择", command=lambda: selectPath("output"))
button3 = Button(root, text="确定转换", command=lambda: changeExcelToCSV(entry1.get(), entry2.get()))

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
button1.grid(row=0, column=2)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=2, column=1)
root.mainloop()