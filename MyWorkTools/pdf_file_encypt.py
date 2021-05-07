from PyPDF2 import PdfFileReader,PdfFileWriter
from pathlib import Path

if __name__ == '__main__':
    src_folder = Path("/src/")
    file_list = list(src_folder.glob("*.pdf"))
    for i in file_list:
        inputfile = PdfFileReader(str(i))
        pageCount = inputfile.getNumPages()
        outputfile = PdfFileWriter()
        for page in range(pageCount):
            outputfile.addPage(inputfile.getPage(page))
        outputfile.encrypt("123456")
        with open(i,'wb') as f:
            outputfile.write(f)