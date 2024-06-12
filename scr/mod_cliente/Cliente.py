from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    logradouro: str
    numero: int
    complemento: str
    bairro: str
    cidade: str
    estado: str
    cep: int
