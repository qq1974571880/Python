import updateURL
import downloadTxt
import Tools.moveToFolder
import Tools.deleteEmptyFromDB


def updatePictures():
    updateURL.updatePictures()
    downloadTxt.downloadPicturesTxt()
    Tools.deleteEmptyFromDB.deletePictures()
    Tools.moveToFolder.choose("文字", "自拍")


if __name__ == '__main__':
    updatePictures()
