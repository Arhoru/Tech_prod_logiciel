def recuperer():
    with open('csv_file/equipements.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        liste_equipements = []
        for row in spamreader:
            liste_equipements.append([row[3], row[4], row[1], row[179], row[178]])
        return liste_equipements
