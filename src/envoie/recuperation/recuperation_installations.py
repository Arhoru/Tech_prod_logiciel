import csv

def recuperer():
    with open('csv_file/installations.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        liste_installations = []
        for row in spamreader:
            liste_installations.append([row[1], row[0], row[6] + ' ' + row[7], row[4], row[2]])
        return liste_installations
