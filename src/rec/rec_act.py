import csv

def recup():
    with open('csv_file/equipements_activites.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        info_act = []
        for row in spamreader:
            info_act.append([row[4], row[5]])
