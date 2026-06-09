# Day 3 – Logging, Exception Handling and Modularization

## Objective

Convert notebook code into reusable project components and understand production-level coding practices.

## Concepts Learned

* Logging
* Exception Handling
* Modular Programming
* Components
* Pipelines

## Tasks Completed

### Learning

1. Learned logging basics.
2. Learned exception handling basics.
3. Created logging experiments.
4. Created exception handling experiments.

### Modularization

5. Created logger.py.
6. Created exception.py.
7. Created data_ingestion.py.
8. Created DataIngestion class.
9. Moved PDF extraction logic from notebook to component.
10. Created ingestion_pipeline.py.
11. Executed extraction through pipeline.

## Workflow

PDF
↓
Data Ingestion Component
↓
Pipeline
↓
Extracted Text

## Files Created

src/logger.py

src/exception.py

src/components/data_ingestion.py

src/pipeline/ingestion_pipeline.py

## Key Learnings

* Notebook code is for experimentation.
* Components contain reusable logic.
* Pipelines connect components together.
* Logging helps track application behavior.
* Exception handling makes applications more robust.

## Next Step

Text Cleaning and Preprocessing.
