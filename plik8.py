from PyPDF2 import PdfFileReader

file = open('ZSI.pdf','rb')
doc = PdfFileReader(file)

print(doc.numPages)
print(doc.isEncrypted)
print(doc.documentInfo)
print(doc.pages[0].extractText())
