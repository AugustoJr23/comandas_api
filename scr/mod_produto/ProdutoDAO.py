from fastapi import APIRouter
from mod_produto.Produto import Produto

# import da persistência
import db
from mod_produto.ProdutoModel import ProdutoDB

# import da segurança
from typing import Annotated
from fastapi import Depends
from security import get_current_active_user, User

# dependências de forma global
router = APIRouter( dependencies=[Depends(get_current_active_user)] )

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produto"])
def get_produto():
    try:
        session = db.Session()

        # busca todos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    except Exception as e:

        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    try:
        session = db.Session()

        # busca um com filtro
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()
        
        return dados, 200
        
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
def post_produto(corpo: Produto):
    try:
        session = db.Session()

        dados = ProdutoDB(None, corpo.nome, corpo.descricao, corpo.foto, corpo.valor_unitario)

        session.add(dados)
        # session.flush()
        session.commit()

        return {"id": dados.id_produto}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, f: Produto):
    return {
        "msg": "put executado", 
        "id": id, 
        "nome": f.nome,
        "descricao": f.descricao,
        "foto": f.foto, 
        "valor_unitario": f.valor_unitario
        }, 201

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()

        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.foto = corpo.foto
        dados.valor_unitario = corpo.valor_unitario

        session.add(dados)
        session.commit()

        return {"id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()

        return {"id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

### Security
@router.get("/funcionario/", tags=["Funcionário"])
def get_produto( current_user:Annotated[User, Depends(get_current_active_user)], ):
    try:
        session = db.Session()

        # busca todos
        dados = session.query(ProdutoDB).all()

        print(current_user)

        return dados, 200

    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
