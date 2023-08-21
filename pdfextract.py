import PyPDF2
import re

pdfFileObj = open("C:\\Users\\dodda\\Downloads\\1BGG882.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
mytext = pageObj.extractText()
filename = r'C:/Users/dodda/Downloads/diskpartioninfo.txt'
lines = mytext.split('\n')
print(lines)
with open(filename, "w") as of:
    for line in lines:
        of.writelines(line + '\n')

vendorinfo = re.findall('Vendor:.*', mytext) 
# print(vendorinfo)
