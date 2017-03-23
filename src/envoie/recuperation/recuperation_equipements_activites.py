import csv

def recuperer():
    with open('csv_file/equipements_activites.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        liste_equipements_activites = []
        for row in spamreader:
            liste_equipements_activites.append([row[2], row[4]])
        return liste_equipements_activites
