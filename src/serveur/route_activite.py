import sqlite3
from serveur.lib.bottle import route, run, debug, template, request, static_file


@route('/activite')
def get_list_activites():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM ACTIVITE")
    result = cursor.fetchall()

    return str(result)

@route('/activite/')
def get_list_activites():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM ACTIVITE")
    result = cursor.fetchall()

    return str(result)
