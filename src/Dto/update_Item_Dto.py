from pydantic import BaseModel

class update_item(BaseModel):
    
    title: str
    description: str