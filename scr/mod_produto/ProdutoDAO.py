from fastapi import APIRouter
from mod_produto.Produto import Produto

router = APIRouter()

# Criar as rotas/endpoints para Produtos: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produto"])
def get_produtos():
    return {"msg": "get todos os produtos executado"}, 200

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    return {"msg": "get um produto executado"}, 200

@router.post("/produto/", tags=["Produto"])
def post_produto(produto: Produto):
    return {
        "msg": "post executado", 
        "nome": produto.nome, 
        "preco": produto.valor_unitario, 
        "descricao": produto.descricao
        }, 200

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, produto: Produto):
    return {
        "msg": "put executado", 
        "id": id, 
        "nome": produto.nome, 
        "preco": produto.valor_unitario, 
        "descricao": produto.descricao
        }, 201

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 201