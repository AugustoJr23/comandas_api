from fastapi import APIRouter
from mod_cliente.Cliente import Cliente

router = APIRouter()

# import da persistência
import db
from mod_cliente.ClienteModel import ClienteDB

router = APIRouter()
# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/funcionario/", tags=["Funcionário"])
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

        dados = ClienteDB(None, corpo.nome, corpo.cpf, corpo.telefone)

        session.add(dados)
        # session.flush()
        session.commit()

        return {"id": dados.id_cliente}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_cliente(id: int, f: Cliente):
    return {
        "msg": "put executado", 
        "id": id, 
        "nome": f.nome, 
        "cpf": f.cpf, 
        "telefone": f.telefone
        }, 201

@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_cliente(id: int, corpo: Cliente):
    try:
        session = db.Session()

        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()

        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone

        session.add(dados)
        session.commit()

        return {"id": dados.id_cliente}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_funcionario(id: int):
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



@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente_by_id(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(cliente: Cliente):
    return {
        "msg": "post executado", 
        "nome": cliente.nome, 
        "matricula": cliente.matricula, 
        "cpf": cliente.cpf, 
        "telefone": cliente.telefone
    }, 200

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, cliente: Cliente):
    return {
        "msg": "put executado", 
        "id": id, 
        "nome": cliente.nome, 
        "matricula": cliente.matricula, 
        "cpf": cliente.cpf, 
        "telefone": cliente.telefone
    }, 201

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201