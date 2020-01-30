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

    link=request.forms.get("link")
    naziv=request.forms.get("naziv")
    velicina=request.forms.get("velicina")
    vrijeme=int(request.forms.get("vrijeme"))
    cijena=int(request.forms.get("cijena"))

    sacuvaj_novu_tetovazu(link,naziv,velicina,vrijeme,cijena)

    redirect('/tattoo')

@app.route('/azuriraj-tattoo')
def azuriraj_tattoo():
    tetovaze_id=request.query['tetovazeid']
    tetovaze=dohvati_tetovazu_po_id(tetovaze_id)
    return template('formatattoo',data=tetovaze, form_akcija="/azuriraj-tattoo-save",template_lookup=[template_path])

@app.route('/azuriraj-tattoo-save',method='POST')
def azuriraj_tattoo_save():
    tetovaze_id=request.forms.get("tetovazeid")
    link=request.forms.get("link")
    naziv=request.forms.get("naziv")
    velicina=request.forms.get("velicina")
    vrijeme=int(request.forms.get("vrijeme"))
    cijena=int(request.forms.get("cijena"))


    azuriraj_tetovazu(tetovaze_id,link,naziv,velicina,vrijeme,cijena)
    redirect('/tattoo')

@app.route('/izbrisi-tattoo')
def izbrisi_tattoo():
    tetovaze_id = request.query['tetovazeid']
    izbrisi_tetovazu(tetovaze_id)
    redirect('/tattoo')

@app.route('/signin')
def signin():
    return template('signin',data=None,form_akcija="/provjera",template_lookup=[template_path])

@app.route('/provjera',method='POST')
def provjera():
    postdata=request.body.read()
    e_mail=request.forms.get("e_mail")
    lozinka=str(request.forms.get("lozinka"))
    svi_korisnici=procitaj_podatke_korisnik()
    for korisnik in svi_korisnici:
        if (korisnik._e_mail==e_mail):
            if (korisnik._lozinka==lozinka):
                tetovaze=procitaj_podatke_tetovaze()
                return template('tattoo',data=tetovaze,template_lookup=[template_path])

            else:
                return template('signin',form_akcija='provjera',template_lookup=[template_path])

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
    korisnik_id=int(request.forms.get("korisnik_id"))
    sacuvaj_novo_osoblje(ime,prezime,datumpocetkarada,brojtetovazaizradenih,korisnik_id)

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
    korisnik_id=int(request.forms.get("korisnik_id"))

    azuriraj_osoblje(osoblje_id,ime,prezime,datumpocetkarada,brojtetovazaizradenih,korisnik_id)
    redirect('/osoblje')

@app.route('/izbrisi-osoblje')
def izbrisi_osoblje_():
    osoblje_id = request.query['osobljeid']
    izbrisi_osoblje(osoblje_id)
    redirect('/osoblje')

@app.route('/racuni')
def racuni():
    podaci=procitaj_podatke_racuna()
    return template('racuni', data=podaci, template_lookup=[template_path])

@app.route('/novi-racun')
def novi_racun():
    return template('formaracuni',data=None,form_akcija="/spremi-racun",template_lookup=[template_path])

@app.route('/spremi-racun', method='POST')
def spremi_racun_():
    postdata=request.body.read()

    datum=request.forms.get("datum")
    osoblje_id=int(request.forms.get("osoblje_id"))
    tetovaze_id=int(request.forms.get("tetovaze_id"))
    ukupno=int(request.forms.get("ukupno"))
    sacuvaj_novi_racun(datum,osoblje_id,tetovaze_id,ukupno)

    redirect('/racuni')

@app.route('/azuriraj-racun')
def azuriraj_racun_():
    racuni_id=request.query['racuniid']
    racuni=dohvati_racun_po_id(racuni_id)
    return template('formaracuni',data=racuni, form_akcija="/azuriraj-racun-save",template_lookup=[template_path])

@app.route('/azuriraj-racun-save',method='POST')
def azuriraj_racun_save():
    racuni_id=request.forms.get("racuniid")
    datum=request.forms.get("datum")
    osoblje_id=int(request.forms.get("osoblje_id"))
    tetovaze_id=int(request.forms.get("tetovaze_id"))
    ukupno=int(request.forms.get("ukupno"))

    azuriraj_racun(racuni_id,datum,osoblje_id,tetovaze_id,ukupno)
    redirect('/racuni')

@app.route('/izbrisi-racun')
def izbrisi_racun_():
    racuni_id = request.query['racuniid']
    izbrisi_racun(racuni_id)
    redirect('/racuni')

run(app, host='localhost', port = 4040)
