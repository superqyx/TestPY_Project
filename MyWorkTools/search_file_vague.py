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
        result = list(folder.rglob(f"*{search_keyword}*"))
        if len(result) == 0:
            print(f"no file:{search_keyword} in {folder}")
        else:
            result_folder = []
            result_file = []
            for i in result:
                if i.is_dir():
                    result_folder.append(i)
                elif i.is_file():
                    result_file.append(i)
                else:
                    print("Wrong")
        if len(result_file) != 0:
            print(f"find {search_keyword} files in {folder}: ")
            for i in result_file:
                print(i)
        if len(result_folder) != 0:
            print(f"find {search_keyword} folder in {folder}")
            for i in result_folder:
                print(i)