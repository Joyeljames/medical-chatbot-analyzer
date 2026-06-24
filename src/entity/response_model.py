from pydantic import BaseModel

class QueryResponse(BaseModel):

    answer:str

class SummaryResponse(BaseModel):

    summary:str