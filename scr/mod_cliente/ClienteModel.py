import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ClienteDB(db.Base):
    __tablename__ = 'tb_cliente'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    matricula = Column(Integer, nullable=False)
    cpf = Column(CHAR(10), nullable=False)
    telefone = Column(CHAR(11), unique=True, nullable=False)

    def __init__(self, id_cliente, nome, matricula, cpf, telefone):
        self.id_cliente = id_cliente
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.telefone = telefone
