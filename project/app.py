from bottle import Bottle, run, \
     template, debug, get, request, redirect, post, route, static_file

import os, sys

from baza import unesi_demo_podatke, procitaj_podatke_tetovaze, sacuvaj_novu_tetovazu, dohvati_tetovazu_po_id, azuriraj_tetovazu, izbrisi_tetovazu

unesi_demo_podatke()
procitaj_podatke_tetovaze()

dirname = os.path.dirname(sys.argv[0])
template_path=dirname+'\\views'
app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.css.map>')
def send_cssmap(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/static/<filename:re:.*\.js.map>')
def send_jsmap(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/')
def index():
    data = {"developer_name": "PMF student",
            "developer_organization": "PMF"}
    return template('index', data = data,template_lookup=[template_path])

@app.route('/about')
def about():
    return template('about')
    
@app.route('/contact')
def contact():
    return template('contact')
   
@app.route('/tattoo')
def tattoo():
    podaci=procitaj_podatke_tetovaze()
    return template('tattoo', data=podaci, template_lookup=[template_path])

@app.route('/signin')
def signin():
    return template('signin')

run(app, host='localhost', port = 4040)
