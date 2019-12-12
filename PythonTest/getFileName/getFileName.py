import sys
import os

# 当前工作路径
print(os.getcwd())  # C:\Github\Python\PythonTest

# 输入参数列表
print(sys.argv)  # ['C:/Github/Python/PythonTest/getFileName.py']

# 第0个就是这个python文件本身的路径（全路径）
print(sys.argv[0])  # C:/Github/Python/PythonTest/getFileName.py

# Python文件名 相当于是上面保留的最后一部分 即*.py
print(sys.argv[0].split('/')[-1].split('.')[0])  # getFileName
