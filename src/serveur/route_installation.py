import sqlite3
import json
from serveur.lib.bottle import route, run, debug, template, request, static_file


@route('/installation')
def get_list_installations():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM INSTALLATION")
    result = cursor.fetchall()

    string_result = str(result)

    string_result = string_result[2:(len(string_result)-2)]

    liste_de_json = []


    for chaine in string_result.split('), ('):
        sous_chaines = chaine.split(',')
        chaine_json = {'id': sous_chaines[0], 'nom': sous_chaines[1], 'adresse': sous_chaines[2], 'code_postal': sous_chaines[3], 'ville': sous_chaines[4]}

        liste_de_json.append(json.loads(json.dumps(chaine_json)))

    liste_json = {'data': json.loads(json.dumps(liste_de_json))}

    return json.dumps(liste_json)



@route('/installation/')
def get_list_installations():
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM INSTALLATION")
    result = cursor.fetchall()

    string_result = str(result)

    string_result = string_result[2:(len(string_result)-2)]

    liste_de_json = []


    for chaine in string_result.split('), ('):
        sous_chaines = chaine.split(',')
        chaine_json = {'id': sous_chaines[0], 'nom': sous_chaines[1], 'adresse': sous_chaines[2], 'code_postal': sous_chaines[3], 'ville': sous_chaines[4]}

        liste_de_json.append(json.loads(json.dumps(chaine_json)))

    liste_json = {'data': json.loads(json.dumps(liste_de_json))}

    return json.dumps(liste_json)



@route('/installation?ville=<ville>')
def get_list_installations(ville):
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM INSTALLATION i WHERE i.VILLE = '"+str(ville)+"'")
    result = cursor.fetchall()

    string_result = str(result)

    string_result = string_result[2:(len(string_result)-2)]

    liste_de_json = []


    for chaine in string_result.split('), ('):
        sous_chaines = chaine.split(',')
        chaine_json = {'id': sous_chaines[0], 'nom': sous_chaines[1], 'adresse': sous_chaines[2], 'code_postal': sous_chaines[3], 'ville': sous_chaines[4]}

        liste_de_json.append(json.loads(json.dumps(chaine_json)))

    liste_json = {'data': json.loads(json.dumps(liste_de_json))}

    return json.dumps(liste_json)



@route('/installation?id_activite=<id_activite>')
def get_list_installations(id_activite):
    connexion = sqlite3.connect('ma_base.db')
    cursor = connexion.cursor()
    cursor.execute("SELECT i1.* FROM INSTALLATION i1, (SELECT e1.NUMERO_INSTALLATION FROM EQUIPEMENT e1, (SELECT * FROM EQUIPEMENT_ACTIVITE WHERE NUMERO_ACTIVITE = " + str(id_activite) + " ) e2 WHERE e1.NUMERO = e2.NUMERO_EQUIPEMENT ) i2 WHERE i1.NUMERO = i2.NUMERO_INSTALLATION")
    result = cursor.fetchall()

    string_result = str(result)

    string_result = string_result[2:(len(string_result)-2)]

    liste_de_json = []


    for chaine in string_result.split('), ('):
        sous_chaines = chaine.split(',')
        chaine_json = {'id': sous_chaines[0], 'nom': sous_chaines[1], 'adresse': sous_chaines[2], 'code_postal': sous_chaines[3], 'ville': sous_chaines[4]}

        liste_de_json.append(json.loads(json.dumps(chaine_json)))

    liste_json = {'data': json.loads(json.dumps(liste_de_json))}

    return json.dumps(liste_json)

    
