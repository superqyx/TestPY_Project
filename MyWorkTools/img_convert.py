from pathlib import Path
from PIL import Image

if __name__ == '__main__':
    src_folder = Path("/src/")
    dest_folder = Path("/dest/")
    if not dest_folder.exists():
        dest_folder.mkdir(parents=True)
    file_list = list(src_folder.glob("*.jpg"))
    for i in file_list:
        dest_file = (dest_folder / i.name).with_suffix(".png")
        Image.open(i).save(dest_file)
        print(f"{i.name} has been converted.")
