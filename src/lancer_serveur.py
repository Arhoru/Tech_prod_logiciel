import sqlite3
from serveur.lib.bottle import route, run, debug, template, request, static_file, app
from serveur.route_activite import *
from serveur.route_equipement import *
from serveur.route_installation import *
from serveur.route_equipement_activite import *
from serveur.route_index import *

def fonction_lancer_serveur(host='localhost' ,port='1234'):
    run(host='localhost' ,port='1234')
