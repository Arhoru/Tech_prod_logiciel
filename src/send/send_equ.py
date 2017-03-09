import ../rec/rec_equ

def send_equ(cursor):

    add_equ = ("INSERT INTO EQUIPEMENT "
                 "(NUMERO, NOM, NUMERO_INSTALLATION, LATITUDE, LONGITUDE) "
                 "VALUES (%d, %s, %d, %f, %f)")

    info_equ = rec_equ.recup
    for row in info_equ:
        cursor.execute(add_equ, row)
