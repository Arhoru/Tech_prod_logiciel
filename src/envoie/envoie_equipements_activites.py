#import recuperation.recuperation_equipements_activites

def envoie_equipements_activites(cursor):

    requete_ajout_equipements_activites = ( "INSERT INTO EQUIPEMENT_ACTIVITE "
                                    "(NUMERO_EQUIPEMENT, NUMERO_INSTALLATION) "
                                    "VALUES (%d, %d)")

    liste_equipements_activites = recuperation_equipements_activites.recuperer
    for row in liste_equipements_activites:
        cursor.execute(requete_ajout_equipements_activites, row)
