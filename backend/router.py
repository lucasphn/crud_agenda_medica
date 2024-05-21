from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import AgendaResponse, AgendaUpdate, AgendaCreate
from schemas_cliente import ClienteResponse, ClienteUpdate, ClienteCreate
from typing import List
from crud import (create_agendamento, get_agendamentos, get_agendamento, delete_agendamento, update_agendamento)
from crud_cliente import (create_cliente, get_clientes, get_cliente, delete_cliente, update_cliente)

'''
Aqui neste arquivo vamos transformar todas as nossas funções do crud em requisições de uma API que irá se comunicar com o nosso banco de dados
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
def delete_agendamento_route(id_agendamento: int, db: Session = Depends(get_db)):
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

## ************************************** INICIANDO API CADASTRO DE CLIENTE ************************************************************

@router.post("/clientes/", response_model=ClienteResponse)
def create_cliente_route(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return create_cliente(db=db, cliente=cliente)

@router.get("/clientes/", response_model=List[ClienteResponse])
def read_all_cliente_route(db: Session = Depends(get_db)):
    clientes = get_clientes(db)
    return clientes

# SELECT de um cliente específico
@router.get("/clientes/{id_cliente}", response_model=ClienteResponse)
def read_cliente_route(id_cliente: int, db: Session = Depends(get_db)):
    db_cliente = get_cliente(db, id_cliente=id_cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado. Tente outro código, por favor.")
    return db_cliente

# DELETE de um cliente específico
@router.delete("/clientes/{id_cliente}", response_model=ClienteResponse)
def delete_cliente_route(id_cliente: int, db: Session = Depends(get_db)):
    db_cliente = delete_cliente(db, id_cliente=id_cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado. Tente outro código, por favor.")
    return db_cliente

# UPDATE de um cliente específico
@router.put("/clientes/{id_cliente}", response_model=ClienteResponse)
def update_cliente_route(id_cliente: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    db_cliente = update_cliente(db, id_cliente=id_cliente, cliente=cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado. Tente outro código, por favor.")
    return db_cliente