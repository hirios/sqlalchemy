from tabelas import Base, Column, Integer, String, Numeric


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    price = Column(Numeric(8, 2), nullable=False)


    def __repr__(self) -> str:
        return f'Produto(name={self.name}, price={self.price})'
