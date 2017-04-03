from import_csv import fonction_import_csv
from lancer_serveur import fonction_lancer_serveur
import os
import os.path

if not os.path.isfile("ma_base.db"):
    fonction_import_csv()

fonction_lancer_serveur()
