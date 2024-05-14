from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import AgendaResponse, AgendaUpdate, AgendaCreate
from typing import List
from crud import (
    create_agendamento,
    get_agendamentos,
    get_agendamento,
    delete_agendamento,
    update_agendamento,
)

'''
Aqui neste arquivo vamos trasnformar todas as nossas funções do crud em requisições de uma API que irá se comunicar com o nosso banco de dados

'''

router = APIRouter()


@router.post("/agenda/", response_model=AgendaResponse)
def create_agenda_route(agendamento: AgendaCreate, db: Session = Depends(get_db)):
    return create_agendamento(db=db, agenda=agendamento)


@router.get("/agenda/", response_model=List[AgendaResponse])
def read_all_agenda_route(db: Session = Depends(get_db)):
    agendamentos = get_agendamentos(db)
    return agendamentos

# SELECT de um agendamento específico
@router.get("/agenda/{id_agendamento}", response_model=AgendaResponse)
def read_agendamento_route(id_agendamento: int, db: Session = Depends(get_db)):
    db_agendamento = get_agendamento(db, id_agendamento=id_agendamento)
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado. Tente outro código, por favor.")
    return db_agendamento

# DELETE de um agendamento específico
@router.delete("/agenda/{id_agendamento}", response_model=AgendaResponse)
def detele_agendamento_route(id_agendamento: int, db: Session = Depends(get_db)):
    db_agendamento = delete_agendamento(db, id_agendamento=id_agendamento)
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado. Tente outro código, por favor.")
    return db_agendamento

# UPDATE de um agendamento específico
@router.put("/agenda/{id_agendamento}", response_model=AgendaResponse)
def update_agendamento_route(id_agendamento: int, agenda: AgendaUpdate, db: Session = Depends(get_db)):
    db_agendamento = update_agendamento(db, id_agendamento=id_agendamento, agenda=agenda)
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado. Tente outro código, por favor.")
    return db_agendamento