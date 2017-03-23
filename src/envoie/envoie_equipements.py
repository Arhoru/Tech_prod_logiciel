from envoie.recuperation import recuperation_equipements

def envoie_equipements(cursor):

    requete_ajout_equipements = ("""INSERT INTO EQUIPEMENT(NUMERO, NOM, NUMERO_INSTALLATION, LATITUDE, LONGITUDE) VALUES (?, ?, ?, ?, ?)""")

    liste_equipements = recuperation_equipements.recuperer
    cursor.executemany(requete_ajout_equipements, liste_equipements())
