from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Persona

import requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///personas.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

datos = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
# archivo = request.get("------------------.json")

datos_json =  datos.json() # paso los datos del archivo a json
# archivo.json()
#documentos = datos_json["docs"]

for pais in datos_json:
    print(len(d.keys()))
    p = Persona(nombre=pais['nombre'], apellido=pais['apellido'], pais=pais['pais'], \
            email=pais['email'])
    session.add(p)

# confirmar transacciones

session.commit()
