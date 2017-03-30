import csv

def recuperer():
    with open('csv_file/equipements_activites.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        liste_activites = []
        for row in spamreader:
            tmp = [row[4], row[5]]
            if tmp not in liste_activites:
                liste_activites.append(tmp)
        return liste_activites
