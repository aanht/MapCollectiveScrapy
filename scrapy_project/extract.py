from PyPDF2 import PdfReader

#pdf file reader object
pdf = PdfReader("2eda3a84bc59fcdb6d72cdbfbb6b63aacbced673.pdf")


#extract text
#grab the page(s) & extract text
page_1_text = pdf.pages[1].extract_text()
print(page_1_text)


# for page in pdf.pages:
#     page_text = page.extract_text()
#     print(page_text)