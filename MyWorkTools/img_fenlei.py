from exifread import process_file
import datetime
from pathlib import Path

if __name__ == '__main__':
    src_folder = Path('/src/')
    dest_folder = Path('/dest/')
    if not dest_folder.exists():
        dest_folder.mkdir(parents=True)
    file_list = list(src_folder.glob("*.jpg"))
    for i in file_list:
        with open(i, 'rb') as f:
            tags = process_file(f,details=False)
            if 'EXTF DateTimeOriginal' in tags.keys():
                dto = str(tags['EXTF DateTimeOriginal'])
                folder_name = datetime.datetime.strptime(dto, '%Y:%m:%d %H:%M:%S').strftime('%Y=%m-%d')
                dest_path = dest_folder / folder_name
                if not dest_path.exists():
                    dest_path.mkdir(parents=True)
                i.replace(dest_path / i.name)