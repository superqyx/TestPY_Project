from filecmp import cmp
from pathlib import Path


if __name__ == '__main__':
    src_folder = Path(input("input the src_folder:"))
    dest_folder = Path(input("input the dest_folder:"))
    if not dest_folder.exists():
        dest_folder.mkdir(parents=True)
    result = list(src_folder.glob("*"))
    file_list = []
    for i in result:
        if i.is_file():
            file_list.append(i)
    for m in file_list:
        for n in file_list:
            if m != n and m.exists() and n.exists():
                if cmp(m,n):
                    n.unlink()

