from sqlalchemy import Column, Integer, String
from src.db.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description= Column(String) 