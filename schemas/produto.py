from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

from schemas import ComentarioSchema


class ProdutoSchema(BaseModel):
    """ Define como um novo presente/inscrito deve ser inserido no banco de dados de eventos.
        Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como inscritos.
    """
    nome: str = "Augusto"
    cpf: Optional[int] = 44455566677
    email: str = "augusto@gmail.com"


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do "produto" (na verdade, presente/inscrito).
        Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como presentes/inscritos.
    """
    nome: str = "Testando..."


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de "produtos" (presentes/inscritos) será retornada.
        Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como presentes/inscritos.
    """
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do "produto" (presentes/inscritos) seguindo o schema definido em
        ProdutoViewSchema.
        Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como presentes/inscritos.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "cpf": produto.cpf,
            "email": produto.email,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um "produto" (presentes/inscritos) será retornado: produto + comentários.
        Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como presentes/inscritos.
    """
    id: int = 1
    nome: str = "Hugo a Gogo"
    cpf: Optional[int] = 44455566677
    email: str = "hugoagogo@gmail.com"
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
        Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como presentes/inscritos.
    """
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do "produto" (inscrito) seguindo o schema definido em
        ProdutoViewSchema.
        Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como presentes/inscritos.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "cpf": produto.cpf,
        "email": produto.email,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
