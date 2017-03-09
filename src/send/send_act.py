import ../rec/rec_act

def send_act(cursor):

    add_act = ("INSERT INTO ACTIVITE "
                 "(NUMERO, NOM) "
                 "VALUES (%d, %s)")

    info_act = rec_act.recup
    for row in info_act:
        cursor.execute(add_act, row)
