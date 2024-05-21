from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional


class ClienteBase(BaseModel):

    nome: str
    data_nascimento: Optional[date]
    cpf: Optional[str]
    uf: Optional[str]
    cidade: Optional[str]
    bairro: Optional[str]
    rua: Optional[str]
    numero: Optional[str]
    email: Optional[EmailStr]
    telefone: Optional[str]

class ClienteCreate(ClienteBase):
    pass 

class ClienteResponse(ClienteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ClienteUpdate(BaseModel):

    nome: Optional[str]
    data_nascimento: Optional[date]
    cpf: Optional[str]
    uf: Optional[str]
    cidade: Optional[str]
    bairro: Optional[str]
    rua: Optional[str]
    numero: Optional[str]
    email: Optional[EmailStr]
    telefone: Optional[str]
 

