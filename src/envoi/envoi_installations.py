from envoi.recuperation import recuperation_installations

def envoi_installations(cursor):

    requete_ajout_installation = ("""INSERT INTO INSTALLATION(NUMERO, NOM, ADRESSE, CODEPOSTAL, VILLE) VALUES (?, ?, ?, ?, ?)""")

    liste_installations = recuperation_installations.recuperer()
    cursor.executemany(requete_ajout_installation, liste_installations)
