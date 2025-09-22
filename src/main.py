
from fastapi import FastAPI, Depends, HTTPException
from src.Dto.add_Item_Dto import Add_Item
from src.Dto.update_Item_Dto import update_item
from sqlalchemy.orm import Session
from src.models.Tickets import Ticket as TicketModel
from src.db.database import Base, engine
from pydantic import BaseModel
from src.config.db_connection import get_db


app = FastAPI()



Base.metadata.create_all(bind=engine)

tickets = []

class Ticket(BaseModel):
    id: int
    title: str
    description: str

 
@app.get('/')
def welcome():
    return {"message": "Welcome to FastAPI application"}

@app.post('/book_Ticket')
def addTicket(Item:Add_Item,db:Session=Depends(get_db)):
    # ticket = Ticket(
    #     id=len(tickets)+1, title=Item.title, description=Item.description
    # )
    # tickets.append(ticket)
    # return {"message": "Ticket added successfully","ticket":Item}  /// in memory persistance
    
    db_ticket= TicketModel(title=Item.title,description=Item.description)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return {"message": "Ticket added successfully","ticket":db_ticket} 



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
def update_ticket(id: int, item: update_item):
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

