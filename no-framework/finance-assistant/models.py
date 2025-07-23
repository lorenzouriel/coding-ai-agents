from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str
    amount: float
    category: str
    date: datetime