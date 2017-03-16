# sources:  https://docs.python.org/3.6/library/csv.html#csv.reader
#           https://docs.python.org/3.6/library/csv.html#csv-fmt-params
#           https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
#           https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

import csv
import mysql.connector
import envoie
import envoie.recuperation

connexion = mysql.connector.connect(user='E155382T', database='E155382T', password='E155382T', host='http://infoweb/phpMyAdmin')
#error 2003 -> probleme de firewall avec le port 3306 utilise par defaut?
cursor = connexion.cursor()

envoie_installations(cursor)
envoie_equipements(cursor)
envoie_activites(cursor)
envoie_equipements_activites(cursor)

connexion.commit()

cursor.close()
connexion.close()
