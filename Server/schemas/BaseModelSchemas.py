from pydantic import BaseModel
from datetime import datetime

class RequestBaseModel(BaseModel):
    data:str
    
    
class ErrorBaseModel(BaseModel):
    success:bool = False
    error:str
    timestamp: str = str(datetime.utcnow())
    
class OutputBaseModel(BaseModel):
    content:str = None
    timestamp: str = str(datetime.utcnow())
    

    