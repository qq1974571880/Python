import re


tmpDownloadTxt = "D:\\CL\\tmpDownloadTxt\\"
tmpDownloadPic = "D:\\CL\\tmpDownloadPic\\"
photoPath = "D:\\CL\\CLPictures\\写真\\"
picturePath = "D:\\CL\\CLPictures\\自拍\\"
photoTxtPath = "D:\\CL\\CLTXT\\写真\\"
pictureTxtPath = "D:\\CL\\CLTXT\\自拍\\"
basicUrl = "https://cb.386i.xyz/"
selfPhotoArea = basicUrl + "thread0806.php?fid=16/"
otherPhotoArea = basicUrl + "thread0806.php?fid=8/"


def rename(name):
    replaceString = r'[\/\\\:\*\?\<\>\|]'
    new_name = re.sub(replaceString, "", name).replace(u'\xa0', u' ').replace('【', '[').replace('】', ']')\
        .replace('\x08','')
    return new_name
