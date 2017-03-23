from envoie.recuperation import recuperation_activites

def envoie_activites(cursor):

    requete_ajout_activite = ("""INSERT INTO ACTIVITE(NUMERO, NOM) VALUES (?, ?)""")

    liste_activite = recuperation_activites.recuperer
    cursor.executemany(requete_ajout_activite, liste_activite())
