import os
import shutil
import pathlib
import filecmp


def getFiles(extendions,src_dir):
    ext_list = extendions.split(',')
    print(ext_list)
    file_list = []
    for ext in ext_list:
        file_list.extend(src_dir.rglob(ext))
    return file_list

def classifyFiles(src_dir, dest_dir,exts):
    src_dir = src_dir
    dest_dir = dest_dir
    exts = exts
    result_files = getFiles(exts, src_dir)
    for i in result_files:
        if i.is_file():
            suffixName = i.suffix.strip('.')
            if not (dest_dir / suffixName).exists():
                (dest_dir / suffixName).mkdir(parents=True)
            if not (dest_dir / i.name).exists():
                i.replace(dest_dir / suffixName / i.name)



'''This is test code'''

if __name__ == '__main__':
    print("This is a file classify function")
    src_dir = pathlib.Path(input("the src_dir:"))
    dest_dir = pathlib.Path(input("the dest_dir:"))
    exts = input("The extendions")
    classifyFiles(src_dir, dest_dir, exts)






