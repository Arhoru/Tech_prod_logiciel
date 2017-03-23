# sources:  https://docs.python.org/3.6/library/csv.html#csv.reader
#           https://docs.python.org/3.6/library/csv.html#csv-fmt-params
#           https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
#           https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

import sqlite3
from envoie import envoie_installations
from envoie import envoie_equipements
from envoie import envoie_activites
from envoie import envoie_equipements_activites

conn = sqlite3.connect('ma_base.db')
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS INSTALLATION(NUMERO INTEGER PRIMARY KEY UNIQUE, NOM TEXT, ADRESSE TEXT, CODEPOSTAL INTEGER, VILLE TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS EQUIPEMENT(NUMERO INTEGER PRIMARY KEY UNIQUE, NOM TEXT, NUMERO_INSTALLATION INTEGER, LATITUDE DECIMAL(3,2), LONGITUDE DECIMAL(3,2))""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ACTIVITE(NUMERO INTEGER PRIMARY KEY UNIQUE, NOM TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS EQUIPEMENT_ACTIVITE(NUMERO_EQUIPEMENT INTEGER, NUMERO_ACTIVITE INTEGER)""")
conn.commit()

envoie_installations.envoie_installations(cursor)
envoie_equipements.envoie_equipements(cursor)
envoie_activites.envoie_activites(cursor)
envoie_equipements_activites.envoie_equipements_activites(cursor)

conn.commit()

conn.close()
