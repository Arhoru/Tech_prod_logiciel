#import recuperation.recuperation_activites

def envoie_activites(cursor):

    requete_ajout_activite = (  "INSERT INTO ACTIVITE "
                        "(NUMERO, NOM) "
                        "VALUES (%d, %s)")

    liste_activites = recuperation_activites.recuperer
    for row in liste_activites:
        cursor.execute(requete_ajout_activite, row)
