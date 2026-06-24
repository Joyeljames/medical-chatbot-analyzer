from langchain_text_splitters import RecursiveCharacterTextSplitter

class textchunk:


    def create_chunks(self,text):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200
        )

        chunks = splitter.create_documents([text])

        return chunks
    
