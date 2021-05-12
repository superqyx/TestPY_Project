import os
import shutil
import pathlib
import filecmp


class MyFileTools(object):
    def __init__(self, src_dir='./', dest_dir='./', suffix_name='*'):
        self._src_dir = pathlib.Path(src_dir)
        self._dest_dir = pathlib.Path(dest_dir)
        self._suffix_name = suffix_name

    @property
    def src_dir(self):
        return self._src_dir
    @src_dir.setter
    def src_dir(self, src_dir):
        if not src_dir.endwith('/'):
            src_dir += '/'
        self._src_dir = pathlib.Path(src_dir)

    @property
    def dest_dir(self):
        return self._dest_dir
    @dest_dir.setter
    def dest_dir(self,dest_dir):
        self._dest_dir = pathlib.Path(dest_dir)

    @property
    def suffix_name(self):
        return self._suffix_name
    @suffix_name.setter
    def suffix_name(self,suffix_name):
        self._suffix_name = suffix_name

    def class_file(self):
        pass


 '''This is test code'''
if __name__ == '__main__':
    print("This is a file classfy function")
    my_file_tool = MyFileTools()





