import sqlite3
import json
from serveur.lib.bottle import route, run, debug, template, request, static_file


@route('/activite')
def get_list_activites():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM ACTIVITE")
    result = cursor.fetchall()

    string_result = str(result)

    string_result = string_result[2:(len(string_result)-2)]

    liste_de_json = []


    for chaine in string_result.split('), ('):
        sous_chaines = chaine.split(',')
        chaine_json = {'id': sous_chaines[0], 'nom': sous_chaines[1]}

        liste_de_json.append(json.loads(json.dumps(chaine_json)))

    liste_json = {'data': json.loads(json.dumps(liste_de_json))}

    return json.dumps(liste_json)



@route('/activite/')
def get_list_activites():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM ACTIVITE")
    result = cursor.fetchall()

    string_result = str(result)

    string_result = string_result[2:(len(string_result)-2)]

    liste_de_json = []


    for chaine in string_result.split('), ('):
        sous_chaines = chaine.split(',')
        chaine_json = {'id': sous_chaines[0], 'nom': sous_chaines[1]}

        liste_de_json.append(json.loads(json.dumps(chaine_json)))

    liste_json = {'data': json.loads(json.dumps(liste_de_json))}

    return json.dumps(liste_json)
