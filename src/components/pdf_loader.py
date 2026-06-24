import fitz

class PdfLoader:
    
    def extract_text(self,filepath):

        document = fitz.open(filepath)

        text =""
        for page in document:
            text += page.get_text()
        
        return text