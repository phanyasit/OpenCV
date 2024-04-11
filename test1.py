import pdfplumber

pdf_filename = "63606015 ปริญญา สกุลอัญมณี is2.pdf"
pdf = pdfplumber.open(pdf_filename)

first_page = pdf.pages[0]
text = first_page.extract_text()
text_filename = pdf_filename+".txt"

f = open(text_filename, "w", encoding="utf-8")
f.write(text)
f.close()