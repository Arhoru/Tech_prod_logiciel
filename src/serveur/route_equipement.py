import sqlite3
import json
from serveur.lib.bottle import route, run, debug, template, request, static_file


@route('/equipement')
def get_list_equipements():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM EQUIPEMENT")
    result = cursor.fetchall()

    string_result = str(result)

    string_result = string_result[2:(len(string_result)-2)]

    liste_de_json = []


    for chaine in string_result.split('), ('):
        sous_chaines = chaine.split(',')
        chaine_json = {'id': sous_chaines[0], 'nom': sous_chaines[1], 'id_installation': sous_chaines[2], 'longitude': sous_chaines[3], 'lattitude': sous_chaines[4]}

        liste_de_json.append(json.loads(json.dumps(chaine_json)))

    liste_json = {'data': json.loads(json.dumps(liste_de_json))}

    return json.dumps(liste_json)



@route('/equipement/')
def get_list_equipements():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM EQUIPEMENT")
    result = cursor.fetchall()

    string_result = str(result)

    string_result = string_result[2:(len(string_result)-2)]

    liste_de_json = []


    for chaine in string_result.split('), ('):
        sous_chaines = chaine.split(',')
        chaine_json = {'id': sous_chaines[0], 'nom': sous_chaines[1], 'id_installation': sous_chaines[2], 'longitude': sous_chaines[3], 'lattitude': sous_chaines[4]}

        liste_de_json.append(json.loads(json.dumps(chaine_json)))

    liste_json = {'data': json.loads(json.dumps(liste_de_json))}

    return json.dumps(liste_json)
