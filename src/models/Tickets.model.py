from sqlalchemy import column, Integer, String
from src.db.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = column(Integer, primary_key=True, index=True)
    title = column(String, index=True)
    description= column(String) 