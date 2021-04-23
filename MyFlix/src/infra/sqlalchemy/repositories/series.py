from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas
from sqlalchemy import select, delete

class RepoSerie():
    
    def __init__(self, db: Session):
        self.db = db

    def create(self, serie: schemas.Serie):
        db_serie = models.Serie(title=serie.title,
                                year=serie.year,
                                genre=serie.genre,
                                number_temp=serie.number_temp)
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)

        return db_serie
    def show(self):
        series = self.db.query(models.Serie).all()
        return series

    def get(self, serie_id: int):
        stmt = select(models.Serie).filter_by(id=serie_id)
        serie = self.db.execute(stmt).one()
        return serie

    def remove(self, serie_id: int):
        stmt = delete(models.Serie).where(models.Serie.id == serie_id)
        
        self.db.execute(stmt)
        self.db.commit()