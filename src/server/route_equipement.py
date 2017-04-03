import sqlite3
from src.server.lib.bottle import route, run, debug, template, request, static_file


@route('/equipement')
def get_list_equipements():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM EQUIPEMENT")
    result = cursor.fetchall()

    return str(result)

@route('/equipement/')
def get_list_equipements():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM EQUIPEMENT")
    result = cursor.fetchall()

    return str(result)
