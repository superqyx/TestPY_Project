import os
import pathlib
import shutil
import hashlib
import cv2


def movefile(src_dir, dest_dir):
    dir_list = os.listdir(src_dir)

    if not dir_list:
        return

    for i in dir_list:
        total_i = src_dir + i
        if os.path.isfile(total_i):
            suffix_name = i.split(".")[-1]
            dir = dest_dir + suffix_name+ '/'
            if not os.path.exists(dir):
                os.mkdir(dir)
            if os.path.exists(dir+i):
                f_src_md5 = hashlib.md5()
                f_dest_md5 = hashlib.md5()
                with open(total_i, 'rb') as f_src:
                    for line in f_src:
                        f_src_md5.update(line)
                with open(dir+i, 'rb') as f_dest:
                    for line in f_dest:
                        f_dest_md5.update(line)
                if f_dest_md5 != f_src_md5:
                    os.rename(total_i,src_dir+str(f_src_md5.hexdigest())+'.'+suffix_name)
                    shutil.move(src_dir+str(f_src_md5.hexdigest())+'.'+suffix_name, dir)
                    print("File move completed,filename:%s" % i)
                    if not os.listdir(os.path.dirname(total_i)):
                        print(os.path.dirname(total_i))
                        os.rmdir(os.path.dirname(total_i))
                else:
                    pass
            else:
                shutil.move(total_i, dir)
                print("File move completed,filename:%s" %i)
                if not os.listdir(os.path.dirname(total_i)):
                    print(os.path.dirname(total_i))
                    os.rmdir(os.path.dirname(total_i))
        elif os.path.isdir(total_i):
            movefile(total_i+'/',dest_dir)
        else:
            return

if __name__ == '__main__':
    src_dir = "C:/tmp/src/"
    dest_dir = "C:/tmp/dest/"
    movefile(src_dir,dest_dir)