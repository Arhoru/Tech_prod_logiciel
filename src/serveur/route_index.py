import sqlite3
from serveur.lib.bottle import route, run, debug, template, request, static_file

@route('/')
def home():
    return static_file('index.html', root='./', mimetype='text/html')
