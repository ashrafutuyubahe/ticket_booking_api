
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tickets = []

class Ticket(BaseModel):
    id: int
    title: str
    description: str

 
@app.get('/')
def welcome():
    return {"message": "Welcome to FastAPI application"}

@app.post('/addTicket')
def addTicket(Item:Ticket):
    tickets.append(Item)
    return {"message": "Ticket added successfully","ticket":Item}

@app.get('/tickets')
def get_tickets():
    return {"tickets": "List of all tickets", "data": tickets}

@app.get("/ticket/{id}")
def get_ticket(id: int):
      for t in tickets:
          if(t.id == id):
              return {
                  "message": "Ticket found",
                  "ticket data": t
              }
      return {
           "message": "Ticket not found"
       }


@app.put("/update/{id}")
def update_ticket(id: int, item: Ticket):
    for t in tickets:
        if(t.id == id):
            t.title = item.title
            t.description = item.description
            return {
                "message": "Ticket updated successfully",
                "ticket data": t
            }
    return {
        "message": "Ticket not found"   
           }

    
