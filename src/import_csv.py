# sources:  https://docs.python.org/3.6/library/csv.html#csv.reader
#           https://docs.python.org/3.6/library/csv.html#csv-fmt-params
#           https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
#           https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

import mysql.connector
import send/send_instal
import send/send_act
import send/send_equ
import send/send_equ_act

connexion = mysql.connector.connect(user='E155382T', database='E155382T', password='E155382T')
cursor = connexion.cursor()

send_instal(cursor)
send_equ(cursor)
send_act(cursor)
send_equ_act(cursor)

connexion.commit()

cursor.close()
connexion.close()
