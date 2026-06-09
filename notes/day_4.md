# Day 4 – Text Cleaning and Preprocessing

## Objective

Clean extracted PDF text and prepare it for chunking and embeddings.

## Concepts Learned

* Text Preprocessing
* Text Normalization
* Whitespace Removal
* Newline Handling
* Pipeline Development

## Tasks Completed

### Notebook Work

1. Created text_preprocessing.ipynb.
2. Loaded extracted text.
3. Calculated character count.
4. Calculated word count.
5. Removed extra spaces.
6. Removed tabs.
7. Removed repeated newlines.
8. Verified cleaned output.
9. Saved cleaned text.

### Modularization

10. Created text_preprocessing.py.
11. Created TextPreprocessor class.
12. Implemented clean_text() method.
13. Created preprocessing_pipeline.py.
14. Processed text through pipeline.
15. Saved clean_report.txt.

### Debugging

16. Fixed module import issues.
17. Learned package execution using python -m.
18. Fixed file path issues.

## Workflow

PDF
↓
Extract Text
↓
Raw Text
↓
Text Preprocessing
↓
Clean Text
↓
Save Output

## Files Created

notebooks/text_preprocessing.ipynb

src/components/text_preprocessing.py

src/pipeline/preprocessing_pipeline.py

artifacts/clean_text/clean_report.txt

## Key Learnings

* PDF text often contains formatting noise.
* Clean text improves downstream NLP tasks.
* Components and pipelines improve maintainability.
* Proper file path handling is important in modular projects.

## Next Step

Chunking the cleaned text into smaller pieces for embeddings and RAG.
