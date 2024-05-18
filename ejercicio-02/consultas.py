from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from generar import Persona

from ingresar import engine

Session = sessionmaker(bind=engine) #conectada  ala coneccion
session = Session()

print("Presentación de todos los países del continente americano")
consulta1 = session.query(Persona).filter(Persona.continent.in_(["NA", "SA"])).all()
for s in consulta1:
    print("%s" % (s.cLDRdisplayname))
print("-----------------------------------------------------------")

print("Presentar los países de Asía, ordenados por el atributo Dial")
consulta2 = session.query(Persona).filter(Persona.continent=="AS").order_by(Persona.dial).all()
for s in consulta2:
    print("%s" % (s.cLDRdisplayname))
print("-----------------------------------------------------------")

print("Presentar los lenguajes de cada país.")
consulta3 = session.query(Persona).all()
for s in consulta3:
    print("Pais:%s - Lenguajes:%s" % (s.cLDRdisplayname,s.languages))
print("-----------------------------------------------------------")

print("Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa")
consulta4 = session.query(Persona).filter(and_(Persona.continent=="EU",Persona.capital!=None)).order_by(Persona.capital).all()
for s in consulta4:
    print("Pais:%s - Capital:%s" % (s.cLDRdisplayname,s.capital))
print("-----------------------------------------------------------")

print("Presentar todos los países que tengan en su cadena de nombre de país uador o en su cadena de capital ito")
consulta5 = session.query(Persona).filter(or_(Persona.cLDRdisplayname.like("%uador%"),Persona.capital.like("%ito%"))).all()
for s in consulta5:
    print("Pais:%s - Capital:%s" % (s.cLDRdisplayname,s.capital))
