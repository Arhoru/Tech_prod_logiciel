import sqlite3
from src.server.lib.bottle import route, run, debug, template, request, static_file
from src.server.route_activite import *
from src.server.route_equipement import *
from src.server.route_installation import *


@route('/')
def home():
    return static_file('index.html', root='./', mimetype='text/html')

run(host='localhost' ,port='1234')
