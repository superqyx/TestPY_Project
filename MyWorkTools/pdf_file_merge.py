from PyPDF2 import PdfFileMerger,PdfFileReader
from pathlib import Path

if __name__ == '__main__':
    src_folder = Path("/src/")
    dest_folder = Path("/dest/")
    if not dest_folder.exists():
        dest_folder.mkdir(parents=True)
    file_list  = list(src_folder.glob("*.pdf"))
    merger = PdfFileMerger()
    outputPage = 0
    for pdf in file_list:
        inputfile = PdfFileReader(str(pdf))
        merger.append(inputfile)
        pageCount = inputfile.getNumPages()
        print(f"{pdf.name} page: {pageCount}")
        outputPage += pageCount
    merger.write(str(dest_folder))
    merger.close()
    print(f"\n the total page numer:{outputPage}")