
from fastapi import FastAPI

app = FastAPI()
 
 
@app.get('/')
def welcome():
    return {"message": "Welcome to FastAPI application"}


@app.get('/tickets')
def get_tickets():
    return {"tickets": ["ticket1", "ticket2", "ticket3"]}


