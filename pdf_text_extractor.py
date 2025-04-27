import fitz 
def extract_text(pdf_path):
    pdf_document=fitz.open(pdf_path)
    text=""
    for page_number in range (len(pdf_document)): #this loop iterates through each page basically yeah
        page=pdf_document.load_page(page_number)
        text+=page.get_text() + "/n"
    return text
pdf_file=r"C:\Users\ayaan\Downloads\demo.pdf"
result=extract_text(pdf_file)
print(result)
