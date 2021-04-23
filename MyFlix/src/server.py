from fastapi import FastAPI, Depends
from src.infra.sqlalchemy.config.database import create_db, get_db
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.series import RepoSerie

app = FastAPI()

create_db()

@app.post('/series')
def create_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    new_serie = RepoSerie(db).create(serie)
    return new_serie

@app.get('/series')
def show_serie(db: Session = Depends(get_db)):
    return RepoSerie(db).show()

@app.get('/series/{serie_id}')
def show_by_id(serie_id: int, db: Session = Depends(get_db)):
    serie = RepoSerie(db).get(serie_id)
    return serie

@app.delete('/series/{serie_id}')
def show_by_id(serie_id: int, db: Session = Depends(get_db)):
    RepoSerie(db).remove(serie_id)
    return {'Msg': "Removed successfuly!"}

