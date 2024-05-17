from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepersonas.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Persona(Base):
    __tablename__ = 'laspersonas'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    pais = Column(String)
    email = Column(String)

    #def __repr__(self):
     #   return "Persona: nombre=%s apellido=%s pais:%s email:%s" % (
      #                    self.nombre,
       #                   self.apellido,
        #                  self.ciudad,
         #                 self.email)


Base.metadata.create_all(engine)

