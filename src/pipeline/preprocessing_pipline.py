from src.components.text_preprocessing import TextPreprocessor


#LOAD REPORT
with open(
    "artifacts/extracted_text/report.txt", "r", encoding="latin-1"
) as f:
    text = f.read()


#PREPROCESSING
process = TextPreprocessor()
clean_text = process.clean_text(text)


#SAVE CLEAN TEXT
with open(
    "artifacts/clean_text/clean_report.txt", "w", encoding="latin-1"
) as f:
    f.write(clean_text)


print("text preprocessing completed successfully.")

