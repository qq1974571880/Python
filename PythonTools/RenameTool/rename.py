import os

minCount = 60
maxCount = 20
path = "./Rename"
filePath = "C:\\Github\\Python\\Rename\\"
basicNewName = "CLPicDownloadTest"
lists = os.listdir(filePath)
maxCount = len(lists) + minCount
print(maxCount)
for i in range(minCount, maxCount):
    os.rename(filePath + lists[i - minCount], filePath + basicNewName + str(i) + ".py")
