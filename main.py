from sqlalchemy import create_engine
from tabelas import Cliente, Produto
from queries.query import ProdutoQuery, ClienteQuery
from tabelas import Base


# CRIA UMA CONEXÃO COM O DB, EXISTENTE OU NÃO
engine = create_engine('sqlite:///test.db', echo=True)
# BASE SÓ É NECESSÁRIA SER EXECUTADA QUANDO O DB NAO EXISTA
Base.metadata.create_all(engine)

# ADICIONANDO USUARIOS 
# user_eduardo = Cliente(name='Eduardo Costa', age=25, email='acolipse@gmail.com')
# ClienteQuery(engine).insert(user_eduardo)

produto_avon = Produto(name='Perfume Amoni Avon', price=65.30)
ProdutoQuery(engine).insert(produto_avon)