from fastapi import APIRouter
from mod_cliente.Cliente import Cliente

# import da persistência
import db
from mod_cliente.ClienteModel import ClienteDB

# import da segurança
from typing import Annotated
from fastapi import Depends
from security import get_current_active_user, User

# dependências de forma global
router = APIRouter( dependencies=[Depends(get_current_active_user)] )

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    try:
        session = db.Session()

        # busca todos
        dados = session.query(ClienteDB).all()
        return dados, 200
    except Exception as e:

        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    try:
        session = db.Session()

        # busca um com filtro
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).all()
        
        return dados, 200
        
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(corpo: Cliente):
    try:
        session = db.Session()

        dados = ClienteDB(None, corpo.nome, corpo.cpf, corpo.logradouro, corpo.numero, corpo.complemento, corpo.bairro, corpo.cidade, corpo.estado, corpo.cep)

        session.add(dados)
        # session.flush()
        session.commit()

        return {"id": dados.id_cliente}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()


@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()

        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()

        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.logradouro = corpo.logradouro
        dados.numero = corpo.numero
        dados.complemento = corpo.complemento
        dados.bairro = corpo.bairro
        dados.cidade = corpo.cidade
        dados.estado = corpo.estado
        dados.cep = corpo.cep

        session.add(dados)
        session.commit()

        return {"id": dados.id_cliente}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    try:
        session = db.Session()

        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        session.delete(dados)
        session.commit()

        return {"id": dados.id_cliente}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()



# verifica se o CPF informado já esta cadastrado, retornado os dados atuais caso já esteja
@router.get("/cliente/cpf/{cpf}", tags=["Cliente - Valida CPF"])
def cpf_cliente(cpf: str):
    try:
        session = db.Session()

        # busca um com filtro, retornando os dados cadastrados
        dados = session.query(ClienteDB).filter(ClienteDB.cpf == cpf).all()

        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201

### Security
@router.get("/cliente/", tags=["Cliente"])
def get_cliente( current_user:Annotated[User, Depends(get_current_active_user)], ):
    try:
        session = db.Session()

        # busca todos
        dados = session.query(ClienteDB).all()

        print(current_user)

        return dados, 200

    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()