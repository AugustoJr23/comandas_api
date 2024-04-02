from pydantic import BaseModel

class Funcionario(BaseModel):
    id_funcionario: int = None
    nome: str
    cpf: str
    telefone: str = None
    senha: str = None
    matricula: str
    grupo: int