import os
import sys
import glob
import uuid


class rename4UUID:
    def __init__(self, path):
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
            os.rename(fname, self.absPath+"/"+renameFname)


if __name__=='__main__':
    dirList = ["bukkake", "ikaten", "kake", "kakiage", "kamaage", "kashiwa"]
    for d in dirList:
        Rename = rename4UUID("../marugame1000/"+d+"/")
        imgList = Rename.grepPicture()
        Rename.renameUUID(imgList)

