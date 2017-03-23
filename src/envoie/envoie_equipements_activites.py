from envoie.recuperation import recuperation_equipements_activites

def envoie_equipements_activites(cursor):

    requete_ajout_equipements_activites = ("""INSERT INTO EQUIPEMENT_ACTIVITE(NUMERO_EQUIPEMENT, NUMERO_ACTIVITE) VALUES (?, ?)""")

    liste_equipements_activites = recuperation_equipements_activites.recuperer
    cursor.executemany(requete_ajout_equipements_activites, liste_equipements_activites())
