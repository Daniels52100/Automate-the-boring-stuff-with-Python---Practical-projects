#! python3
# This program encrypts every .pdf file in a folder and 
# tries to access all the pdfs in folder to make sure they
# were encrypted

import PyPDF2, os, sys
try:
    path, key = sys.argv[1:]
    os.chdir(path)

    # Searching for PDFs:
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            try:
                # Creating PDF reader and writer object:
                print('Encrypting %s...' % (filename))
                pdfFile = open(filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                encrypted = PyPDF2.PdfFileWriter()

                # Copying content:
                for pageNum in range(pdfReader.numPages):
                    page = pdfReader.getPage(pageNum)
                    encrypted.addPage(page)
                
                # Encrypting:
                encrypted.encrypt(key)

                # Creating new PDF:
                encryptedFile = open(filename[:-4] + '_encrypted.pdf', 'wb')
                encrypted.write(encryptedFile)
                encryptedFile.close()
                pdfFile.close()
                print('    Done.')

                # Deleting unencrypted pdf:
                os.unlink(filename)

            except PyPDF2.utils.PdfReadError:
                print('    %s is already encrypted.' % (filename))

    # Verifying encryption:
    print('Verifying encryption...')
    allEncrypted = True
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            if not pdfReader.isEncrypted:
                print('WARNING: %s is not encrypted.' % filename)
                allEncrypted = False
    if allEncrypted:
        print('    All files are encrypted. Safe and sound.')

except (ValueError, IndexError, FileNotFoundError):
    print('Something went wrong. How to use:')
    print('    The first argument is the path to the folder containing the .pdf files;')
    print('    The second argument is the key which will encrypt all folders.')