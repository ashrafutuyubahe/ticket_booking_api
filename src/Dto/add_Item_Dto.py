from pydantic import BaseModel


class Add_Item(BaseModel):
    id: int
    title: str
    description: str


