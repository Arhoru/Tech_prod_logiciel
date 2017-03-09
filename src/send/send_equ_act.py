import ../rec/rec_equ_act

def send_equ_act(cursor):

    add_equ_act = ("INSERT INTO EQUIPEMENT_ACTIVITE "
                 "(NUMERO_EQUIPEMENT, NUMERO_INSTALLATION) "
                 "VALUES (%d, %d)")

    info_equ_act = rec_equ_act.recup
    for row in info_equ_act:
        cursor.execute(add_equ_act, row)
