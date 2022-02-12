from sqlalchemy.orm import declarative_base


# A BASE É DECLARADA ANTES DAS IMPORTAÇÕES
# PRA QUE "Produto" e "Cliente" POSSAM HERDÁ-LA

Base = declarative_base()
from sqlalchemy import Column, Integer, String, Numeric
from .produto import Produto
from .cliente import Cliente