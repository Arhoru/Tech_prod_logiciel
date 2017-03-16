#import recuperation.recuperation_installations

def envoie_installations(cursor):

    requete_ajout_installation = (  "INSERT INTO INSTALLATION "
                                    "(NUMERO, NOM, ADRESSE, CODEPOSTAL, VILLE) "
                                    "VALUES (%d, %s, %s, %d, %s)")

    liste_installations = recuperation_installations.recuperer
    for row in liste_installations:
        cursor.execute(requete_ajout_installation, row)
