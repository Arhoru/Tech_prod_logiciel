def recuperer():
    with open('csv_file/equipements_activites.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        liste_activites = []
        for row in spamreader:
            liste_activites.append([row[4], row[5]])
        return liste_activites
