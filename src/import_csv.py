# sources:  https://docs.python.org/3.6/library/csv.html#csv.reader
#           https://docs.python.org/3.6/library/csv.html#csv-fmt-params
#           https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
#           https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

import sqlite3
import os
from envoi import envoi_installations
from envoi import envoi_equipements
from envoi import envoi_activites
from envoi import envoi_equipements_activites

os.remove('ma_base.db')
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS INSTALLATION(NUMERO INTEGER PRIMARY KEY UNIQUE, NOM TEXT, ADRESSE TEXT, CODEPOSTAL INTEGER, VILLE TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS EQUIPEMENT(NUMERO INTEGER PRIMARY KEY UNIQUE, NOM TEXT, NUMERO_INSTALLATION INTEGER, LATITUDE REAL, LONGITUDE REAL)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ACTIVITE(NUMERO INTEGER PRIMARY KEY UNIQUE, NOM TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS EQUIPEMENT_ACTIVITE(NUMERO_EQUIPEMENT INTEGER, NUMERO_ACTIVITE INTEGER)""")
conn.commit()

envoi_installations.envoi_installations(cursor)
envoi_equipements.envoi_equipements(cursor)
envoi_activites.envoi_activites(cursor)
envoi_equipements_activites.envoi_equipements_activites(cursor)

conn.commit()

conn.close()
