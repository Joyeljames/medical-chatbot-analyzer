from src.components.data_ingestion import DataIngestion

obj = DataIngestion()

text = obj.extract_text_from_pdf("data/raw/sample_medical_report.pdf")

print(text[:500])

with open("artifacts/extracted_text/report.txt","w") as f:
    f.write(text)