import sqlite3
from serveur.lib.bottle import route, run, debug, template, request, static_file


@route('/equipement_activite')
def get_list_equipements_activites():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM EQUIPEMENT_ACTIVITE")
    result = cursor.fetchall()

    return str(result)

@route('/equipement_activite/')
def get_list_equipements_activites():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM EQUIPEMENT_ACTIVITE")
    result = cursor.fetchall()

    return str(result)