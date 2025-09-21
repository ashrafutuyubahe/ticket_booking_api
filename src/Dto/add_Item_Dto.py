from pydantic import BaseModel


class Add_Item(BaseModel):
    
    title: str
    description: str


