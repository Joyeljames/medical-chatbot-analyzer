from src.components.summary_generator import SummaryGenerator

with open("artifacts/clean_text/clean_report.txt",
          "r",
          encoding="latin-1") as f:

    text = f.read()



summarizer = SummaryGenerator()

summary =summarizer.generate_summary(text)

print(summary)