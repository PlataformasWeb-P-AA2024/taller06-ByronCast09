from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///personas.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Persona(Base):
    __tablename__ = 'laspersonas'
    
    id = Column(Integer, primary_key=True)
    cLDRdisplayname = Column(String)
    capital = Column(String)
    continent = Column(String)
    dial = Column(String)
    geonameID = Column(Integer)
    iTU= Column(String)
    languages= Column(String)
    is_independent= Column(String)
    def __repr__(self):
        return "Persona: nombre PAis=%s capital=%s continente:%s DIal:%s GeonameID:%d ITU:%s Lenguajes:%s ES indepentdiente?:%s" % (
                          self.cLDRdisplayname,
                          self.capital,
                          self.continent,
                          self.dial,
                          self.geonameID,
                          self.iTU,
                          self.languages,
                          self.is_independent)


Base.metadata.create_all(engine)
