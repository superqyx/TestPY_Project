import os
import shutil
import pathlib
import filecmp
import PIL


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

def replaceDuplicatFiles(flag, src_dir, dest_dir=None):
    if flag == 0 and dest_dir is None:
        return False

    try:
        src_dir = src_dir
        if not src_dir.exists():
            raise Exception(f"The {src_dir} is not exists.")
        if not src_dir.is_dir():
            raise Exception(f"The {src_dir} is not directory.")
        dest_dir = dest_dir
        result = list(src_dir.glob('*'))
        file_list = []
        for i in result:
            if i.is_file():
                file_list.append(i)
        for m in file_list:
            for n in file_list:
                if m != n and m.exists() and n.exists():
                    if filecmp.cmp(m,n):
                        if flag == 0:
                            if not dest_dir.exists():
                                dest_dir.mkdir(parents=True)
                            if not (dest_dir/n.name).exists():
                                print(dest_dir/n.name)
                                n.replace(dest_dir / n.name)
                        else:
                            n.unlink()
    except Exception as e:
        print("The program has something wrong:",e)



'''This is test code'''

if __name__ == '__main__':
    # print("This is a file classify function")
    # src_dir = pathlib.Path(input("the src_dir:"))
    # dest_dir = pathlib.Path(input("the dest_dir:"))
    # exts = input("The extendions")
    # classifyFiles(src_dir, dest_dir, exts)
    src_dir = pathlib.Path(r'/Users/quyx/Documents/Code/Python/TestPY_Project/src/')
    dest_dir = pathlib.Path(r'/Users/quyx/Documents/Code/Python/TestPY_Project/dest/')
    replaceDuplicatFiles(1,src_dir,dest_dir)






