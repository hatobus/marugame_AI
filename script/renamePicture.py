import os
import sys
import glob
import uuid


class rename4UUID:
    def __init__(self, path<`3`>):
        self.dirPath = path

    def grepPicture(self):
        self.absPath = os.path.abspath(self.dirPath)
        imageList = glob.glob(os.path.join(self.absPath, "*.jpg"))
        return imageList

    def renameUUID(self, imgList):
        #Using UUID4
        for fname in imgList:
            _path, _fname = os.path.split(fname)
            root, ext = os.path.splitext(_fname)
            renameFname = str(uuid.uuid4()).split("-")[-1] + ext
            os.rename(fname, _path+renameFname)


if __name__=='__main__':
    Rename = rename4UUID("path/to/rename")
    imgList = Rename.grepPicture()
    Rename.renameUUID(imgList)

