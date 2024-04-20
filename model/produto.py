from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Produto(Base):
    __tablename__ = 'produto'

    # Ajustes nas colunas para trocá-las para CPF e email,
    # a fim de estarem compatíveis com o App EventReg
    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    cpf = Column(Integer)
    email = Column(String(140), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o "produto" (presente/inscrito) e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto' (presente/inscrito),
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    # Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como inscritos.
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, cpf:int, email:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto (ou melhor, um inscrito)

        Arguments:
            nome: nome do inscrito no evento.
            cpf: CPF do inscrito no evento (opcional, por causa da LGPD)
            email: endereço de e-mail do inscrito
            data_insercao: data de quando o inscrito foi inserido à base
            OBS.: Apesar do nome da classe, métodos e variáveis ter o nome produto, entenda-se como presentes/inscritos.
        """
        self.nome = nome
        self.cpf = cpf
        self.email = email

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Produto
        """
        self.comentarios.append(comentario)

