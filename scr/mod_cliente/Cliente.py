from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    matricula: int
    cpf: str
    telefone: str = None