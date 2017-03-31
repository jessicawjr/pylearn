import os


class Directory(object):
    def __init__(self, fpath):
        self.fullpath = fpath

    def getbasename(self):
        self.basename = os.path.basename(self.fullpath)
        return self.basename

    def getdirname(self):
        self.dirname = os.path.dirname(self.fullpath)
        return self.dirname


if __name__ == "__main__":
    oripath = '/Users/jessicawjr/Desktop/test1.txt'
    d = Directory(oripath)
    print(d.getbasename())
    print(d.getdirname())
