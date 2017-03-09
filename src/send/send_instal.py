import ../rec/rec_instal

def send_instal(cursor):

    add_instal = ("INSERT INTO INSTALLATION "
                 "(NUMERO, NOM, ADRESSE, CODEPOSTAL, VILLE) "
                 "VALUES (%d, %s, %s, %d, %s)")

    info_instal = rec_instal.recup
    for row in info_instal:
        cursor.execute(add_instal, row)
