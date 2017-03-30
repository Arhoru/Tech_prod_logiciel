import sqlite3
from src.lib.bottle import route, run, debug, template, request, static_file

@route('/activites')
def get_list_activites():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM ACTIVITE")
    result = cursor.fetchall()
    
    return str(result)

@route('/activites/')
def get_list_activites():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM ACTIVITE")
    result = cursor.fetchall()

    return str(result)

@route('/')
def home():
    return static_file('index.html', root='./', mimetype='text/html')

run(host='localhost' ,port='1234')
