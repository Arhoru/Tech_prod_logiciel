#import recuperation.recuperation_equipements

def envoie_equipements(cursor):

    requete_ajout_equipements = (   "INSERT INTO EQUIPEMENT "
                            "(NUMERO, NOM, NUMERO_INSTALLATION, LATITUDE, LONGITUDE) "
                            "VALUES (%d, %s, %d, %f, %f)")

    liste_equipements = recuperation_equipements.recuperer
    for row in liste_equipements:
        cursor.execute(requete_ajout_equipements, row)
