import sqlite3
from src.server.lib.bottle import route, run, debug, template, request, static_file


@route('/installation')
def get_list_installations():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM INSTALLATION")
    result = cursor.fetchall()

    return str(result)

@route('/installation/')
def get_list_installations():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM INSTALLATION")
    result = cursor.fetchall()

    return str(result)

@route('/installation/ville/<ville>')
def get_list_installations(ville):
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM INSTALLATION i WHERE i.VILLE = '"+str(ville)+"'")
    result = cursor.fetchall()

    return str(result)

@route('/installation/activite/<activite>')
def get_list_installations(activite):
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM INSTALLATION i1, (SELECT NUMERO_INSTALLATION, NUMERO FROM EQUIPEMENT e1, (SELECT * FROM EQUIPEMENT_ACTIVITE WHERE NUMERO_ACTIVITE = '"+str(activite)+"' ) e2 WHERE e1.NUMERO = e2.NUMERO_EQUIPEMENT) i2 WHERE i1.NUMERO = i2.NUMERO))")
    result = cursor.fetchall()

    return str(result)
