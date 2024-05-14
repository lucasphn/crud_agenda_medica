from sqlalchemy.orm import Session
from schemas import AgendaUpdate, AgendaCreate
from models import AgendaModel

def get_agendamento(db: Session, id_agendamento: int):
    """
    função que recebe um id e retorna somente ele
    """
    return db.query(AgendaModel).filter(AgendaModel.id == id_agendamento).first()

def get_agendamentos(db: Session):
    """
    função que retorna todos os elementos
    """
    return db.query(AgendaModel).all()

def create_agendamento(db: Session, agenda: AgendaCreate):
    """
    função que insere um novo agendamento no banco
    """
    db_agendamento = AgendaModel(**agenda.model_dump())
    db.add(db_agendamento)
    db.commit()
    db.refresh(db_agendamento)
    return db_agendamento

def delete_agendamento(db: Session, id_agendamento: int):
    """
    função que deleta um agendamento no banco
    """
    db_agendamento = db.query(AgendaModel).filter(AgendaModel.id == id_agendamento).first()
    db.delete(db_agendamento)
    db.commit()
    return db_agendamento

def update_agendamento(db: Session, id_agendamento: int, agenda: AgendaUpdate):
    """
    função que atualiza um agendamento específico
    """
    db_agendamento = db.query(AgendaModel).filter(AgendaModel.id == id_agendamento).first()

    if db_agendamento is None:
        return None

    if agenda.data_agendada is not None:
        db_agendamento.data_agendada = agenda.data_agendada
    if agenda.hora_agendada is not None:
        db_agendamento.hora_agendada = agenda.hora_agendada
    if agenda.nome_paciente is not None:
        db_agendamento.nome_paciente = agenda.nome_paciente
    if agenda.nome_medico is not None:
        db_agendamento.nome_medico = agenda.nome_medico
    if agenda.categoria_agendamento is not None:
        db_agendamento.categoria_agendamento = agenda.categoria_agendamento
    if agenda.price is not None:
        db_agendamento.price = agenda.price
    if agenda.email_paciente is not None:
        db_agendamento.email_paciente = agenda.email_paciente
    if agenda.description is not None:
        db_agendamento.description = agenda.description

    db.commit()
    return db_agendamento