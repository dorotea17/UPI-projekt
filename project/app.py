from bottle import Bottle, run, \
     template, debug, get, request, redirect, post, route, static_file

import os, sys

from baza import *

unesi_demo_podatke()
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

@app.route('/nova-tattoo')
def nova_tetovaza():
    return template('formatattoo',data=None,form_akcija="/spremi-tattoo",template_lookup=[template_path])

@app.route('/spremi-tattoo', method='POST')
def spremi_tattoo():
    postdata=request.body.read()

    naziv=request.forms.get("naziv")
    velicina=request.forms.get("velicina")
    vrijeme=int(request.forms.get("vrijeme"))
    cijena=int(request.forms.get("cijena"))

    sacuvaj_novu_tetovazu(naziv,velicina,vrijeme,cijena)

    redirect('/tattoo')

@app.route('/azuriraj-tattoo')
def azuriraj_tattoo():
    tetovaze_id=request.query['tetovazeid']
    tetovaze=dohvati_tetovazu_po_id(tetovaze_id)
    return template('formatattoo',data=tetovaze, form_akcija="/azuriraj-tattoo-save",template_lookup=[template_path])

@app.route('/azuriraj-tattoo-save',method='POST')
def azuriraj_tattoo_save():
    tetovaze_id=request.forms.get("tetovazeid")
    naziv=request.forms.get("naziv")
    velicina=request.forms.get("velicina")
    vrijeme=int(request.forms.get("vrijeme"))
    cijena=int(request.forms.get("cijena"))


    azuriraj_tetovazu(tetovaze_id,naziv,velicina,vrijeme,cijena)
    redirect('/tattoo')

@app.route('/izbrisi-tattoo')
def izbrisi_tattoo():
    tetovaze_id = request.query['tetovazeid']
    izbrisi_tetovazu(tetovaze_id)
    redirect('/tattoo')

@app.route('/signin')
def signin():
    return template('signin')

@app.route('/osoblje')
def osoblje():
    podaci=procitaj_podatke_osoblja()
    return template('osoblje', data=podaci, template_lookup=[template_path])

@app.route('/novo-osoblje')
def novo_osoblje():
    return template('formaosoblje',data=None,form_akcija="/spremi-osoblje",template_lookup=[template_path])

@app.route('/spremi-osoblje', method='POST')
def spremi_osoblje():
    postdata=request.body.read()

    ime=request.forms.get("ime")
    prezime=request.forms.get("prezime")
    datumpocetkarada=request.forms.get("datumpocetkarada")
    brojtetovazaizradenih=int(request.forms.get("brojtetovazaizradenih"))

    sacuvaj_novo_osoblje(ime,prezime,datumpocetkarada,brojtetovazaizradenih)

    redirect('/osoblje')

@app.route('/azuriraj-osoblje')
def azuriraj_osoblje_():
    osoblje_id=request.query['osobljeid']
    osoblje=dohvati_osoblje_po_id(osoblje_id)
    return template('formaosoblje',data=osoblje, form_akcija="/azuriraj-osoblje-save",template_lookup=[template_path])

@app.route('/azuriraj-osoblje-save',method='POST')
def azuriraj_osoblje_save():
    osoblje_id=request.forms.get("osobljeid")
    ime=request.forms.get("ime")
    prezime=request.forms.get("prezime")
    datumpocetkarada=request.forms.get("datumpocetkarada")
    brojtetovazaizradenih=int(request.forms.get("brojtetovazaizradenih"))

    azuriraj_osoblje(osoblje_id,ime,prezime,datumpocetkarada,brojtetovazaizradenih)
    redirect('/osoblje')

@app.route('/izbrisi-osoblje')
def izbrisi_osoblje_():
    osoblje_id = request.query['osobljeid']
    izbrisi_osoblje(osoblje_id)
    redirect('/osoblje')

run(app, host='localhost', port = 4040)
