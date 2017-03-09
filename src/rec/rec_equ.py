import csv

def recup():
    with open('csv_file/equipements.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        info_equip = []
        for row in spamreader:
            info_equip.append([row[3], row[4], row[1], row[179], row[178]])
