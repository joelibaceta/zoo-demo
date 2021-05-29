from ..database import Base
from sqlalchemy import Column, Integer, String, Float

class Zoo(Base):
    __tablename__='zoo'

    idzoo = Column(Integer, primary_key=True)
    nombre = Column(String)
    ciudad = Column(String)
    tamano_m2 = Column(Float)
    presupuesto_anual = Column(Float)
    
    