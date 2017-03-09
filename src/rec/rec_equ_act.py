import csv

def recup():
    with open('csv_file/equipements_activites.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        info_act_equ = []
        for row in spamreader:
            info_act_equ.append([row[2], row[4]])
