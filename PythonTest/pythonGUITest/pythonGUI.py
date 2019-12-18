from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PythonTools.ExcelToCSVTool.ExcelToCSVTool import runProject


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
