import PyPDF2
import sys

input_pdfs = sys.argv[1:]
input_pdfs_list = list(input_pdfs)
print("I hope you only chose pdfs not watermarks previously")
print("this script will automatically create a new merged pdf.")
mergedpdfname = input("choose your output pdf name: ")
wtr = input("choose your watermark pdf: ")


def pdf_combiner_wtr(pdf_list):
    global wtr
    global mergedpdfname
    merger = PyPDF2.PdfFileMerger()
    wtrf = wtr
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')
    output = PyPDF2.PdfFileWriter()
    wtry = PyPDF2.PdfFileReader(open(wtrf, 'rb'))
    pdfy = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
    for i in range(pdfy.getNumPages()):
        print(i)
        watermark = wtry.getPage(0)
        page = pdfy.getPage(i)
        page.mergePage(watermark)
        output.addPage(page)
        with open(mergedpdfname, "wb") as filehandle_output:
            output.write(filehandle_output)


pdf_combiner_wtr(input_pdfs_list)


