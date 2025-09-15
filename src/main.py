
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Ticket(BaseModel):
    id: int
    title: str
    description: str

 
@app.get('/')
def welcome():
    return {"message": "Welcome to FastAPI application"}

@app.post('/addTicket')
def addTicket(Item:Ticket):
    id= Item.id
    title= Item.title
    description= Item.description
    Ticket(id, title, description
            )
#     return {"message": "Ticket added successfully","ticket":Ticket}

# @app.get('/tickets')
# def get_tickets():
#     return {"tickets": "List of all tickets", "data": Ticket}
 
# @app.get("/ticket/:id")
# def get_ticket(id: int):
#     return {
#         "ticket data:" : Ticket.id == id
#     }
    
# @app.put("/update/:id")
# def update_ticket(id: int, item: Ticket):
#     for id in Ticket:
#         if(Ticket.id == id):
#             Ticket.title = item.title
#             Ticket.description = item.description
#             break
#     return {
#         "message": "Ticket updated successfully",
#         "ticket data": Ticket.id == id
#     }
    
