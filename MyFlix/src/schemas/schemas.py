from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):
    id: Optional[int] = None
    title: str
    year: int
    genre: str
    number_temp: int

    class Config:
        orm_mode = True


