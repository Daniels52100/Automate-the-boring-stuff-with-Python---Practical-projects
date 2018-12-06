# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF.
import PyPDF2, os
# Get all the PDF filenames.
pdfFiles = []
os.chdir('.\\automate_online-materials')
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
# Loop through all the PDF files.
for filename in pdfFiles:
    try:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # Loop through all the pages (except the first) and add them.
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    except PyPDF2.utils.PdfReadError:
        continue # skipping encrypted files.

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()