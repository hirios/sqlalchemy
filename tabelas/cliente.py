from tabelas import Base, Column, Integer, String, Numeric


class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(80), unique=True, nullable=False)


    def __repr__(self) -> str:
        return f'Cliente(name={self.name}, email={self.email})'
