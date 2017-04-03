import csv

def recuperer():
    with open('csv_file/equipements.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        liste_equipements = []
        for row in spamreader:
            liste_equipements.append([row[4], row[3], row[2], row[180], row[179]])
        return liste_equipements
