import fitz

class DataIngestion:
    def extract_text_from_pdf(self,file_path):
        text = ""
        pdf_doc = fitz.open(file_path)
        for page_num in range(len(pdf_doc)):
            page = pdf_doc.load_page(page_num)
            text += page.get_text()
        pdf_doc.close()
        return text