import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ClienteDB(db.Base):
    __tablename__ = 'tb_cliente'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    cpf = Column(CHAR(10), nullable=False)
    logradouro = Column(CHAR(100), nullable=False)
    numero = Column(Integer, nullable=False)
    complemento = Column(CHAR(100), nullable=False)
    bairro = Column(CHAR(100), nullable=False)
    cidade = Column(CHAR(100), nullable=False)
    estado = Column(CHAR(100), nullable=False)
    cep = Column(Integer, nullable=False)

    def __init__(self, id_cliente, nome, cpf, logradouro, numero, complemento, bairro, cidade, estado, cep):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

