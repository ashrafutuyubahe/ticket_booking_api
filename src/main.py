from fastapi import FastAPI
from pydantic import BaseModel
from src.Dto.add_Item_Dto import Add_Item

app = FastAPI()

tickets = []

class Ticket(BaseModel):
    id: int
    title: str
    description: str

 
@app.get('/')
def welcome():
    return {"message": "Welcome to FastAPI application"}

@app.post('/book_Ticket')
def addTicket(Item:Add_Item):
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


@app.delete("/unbook/{id}")
def delete_ticket(id: int):
        
         for t in tickets:
             
          if(t.id == id):
             tickets.remove(t)
             return {
                 "message": "Ticket deleted successfully"
             }
         return {
        "message": "Ticket not found"
    }

