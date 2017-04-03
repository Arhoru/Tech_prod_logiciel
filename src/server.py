import sqlite3
from lib.bottle import route, run, debug, template, request, static_file
from server.route_activite import *
from server.route_equipement import *
from server.route_installation import *
from server.route_equipement_activite import *


@route('/')
def home():
    return static_file('index.html', root='./', mimetype='text/html')

run(host='localhost' ,port='1234')
