from sqlalchemy.orm import Session
from tabelas import Produto, Cliente
from typing import Union


class ProdutoQuery():
    def __init__(self, engine):
        self.engine = engine


    # ADICIONA UM PRODUTO
    def insert(self, instancia_produto: Produto) -> None:
        with Session(self.engine) as session:
            session.add(instancia_produto)
            session.commit()


class ClienteQuery():
    def __init__(self, engine):
        self.engine = engine


    # ADICIONA UM CLIENTE
    def insert(self, instancia_cliente: Cliente) -> None:
        with Session(self.engine) as session:
            session.add(instancia_cliente)
            session.commit()            