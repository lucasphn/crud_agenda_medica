from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from sqlalchemy.sql import func
from database import Base

class AgendaModel(Base):
    __tablename__ = 'agenda_medica'  # esse será o nome da tabela

    id = Column(Integer, primary_key=True, index=True)
    data_agendada = Column(Date, index=True)
    hora_agendada = Column(String, index=True)
    nome_paciente = Column(String, index=True)
    nome_medico = Column(String, index=True)
    categoria_agendamento = Column(String, index=True)
    price = Column(Float, index=True)
    email_paciente = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)