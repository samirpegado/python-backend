from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base

class Serie(Base):
    __tablename__ = 'serie'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    genre = Column(String)
    number_temp = Column(Integer)
