import csv

def recup():
    with open('csv_file/installations.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        info_instal = []
        for row in spamreader:
            info_instal.append([row[1], row[0], row[6] + ' ' + row[7], row[4], row[2]])
        return info_instal
