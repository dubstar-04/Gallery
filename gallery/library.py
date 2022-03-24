from os import listdir
from os.path import isfile, join
from pathlib import Path


class Library():

    def __init__(self):
        self.images = []
        self.imageTypes = []
        self.path = str(join(Path.home(), "Pictures"))

    def LoadImages(self):
        print("Path:", self.path)
        path = self.path
        images = []
        for f in listdir(path):
            filePath = join(path, f)
            if isfile(filePath):
                images.append(filePath)


        print("files:", images)
        return images
        
