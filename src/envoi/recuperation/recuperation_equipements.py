import csv

def recuperer():
    with open('csv_file/equipements.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        liste_equipements = []
        for row in spamreader:
            tmp = [row[4], row[3], row[1], row[179], row[178]]
            if tmp not in liste_equipements and len(tmp) != 0:
                liste_equipements.append(tmp)
        return liste_equipements
