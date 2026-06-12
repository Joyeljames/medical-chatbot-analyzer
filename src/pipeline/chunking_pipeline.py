from src.components.chunking import textchunk
import pickle

with open("artifacts/clean_text/clean_report.txt","r",
          encoding="latin-1"
          ) as f:
    
    text = f.read()


chunker  = textchunk()

chunking = chunker.create_chunks(text)

print("total_chunks",len(chunking))


#save chunk

with open(
    "artifacts/chunks/chunking_report.pkl","w",
    encoding="latin-1"
) as f:
    for i,chunk in enumerate(chunking):
        f.write(f"\n\n ====== {i+1} =====\n")
        f.write(chunk)

print("done")
