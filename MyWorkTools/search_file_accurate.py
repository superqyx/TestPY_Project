from pathlib import Path



if __name__ == '__main__':
    while True:
        folder = input("input the folder:")
        folder = Path(folder.strip())
        if folder.exists() and folder.is_dir():
            pass
        else:
            print("folder is wrong")
        search_keyword = input("input the keyword:")
        result = list(folder.rglob(search_keyword))
        if len(result) == 0:
            print(f"no file:{search_keyword} in {folder}")
        else:
            print(f"Find file:{search_keyword} in {folder}:")
            for i in result:
                print(i)