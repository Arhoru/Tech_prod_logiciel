import csv

def recuperer():
    with open('csv_file/equipements_activites.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        liste_equipements_activites = []
        for row in spamreader:
            tmp = [row[2], row[4]]
            if tmp not in liste_activites:
                liste_activites.append(tmp)
        return liste_equipements_activites
