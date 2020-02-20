from bottle import Bottle, run, \
     template, debug, get, request, redirect, post, route, static_file

import os, sys

from baza import *

unesi_demo_podatke()
procitaj_podatke_tetovaze()
procitaj_podatke_racuna()
procitaj_podatke_osoblja()
procitaj_podatke_korisnik()
trenutnikorisnik=""
trenutnoosoblje=""
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

@app.route('/signkorisnici')
def signkorisnik():
    return template('signin',data=None,form_akcija="provjerak",template_lookup=[template_path])

@app.route('/provjerak',method=['GET','POST'])
def provjerakorisnika():
    global trenutnikorisnik
    postdata=request.body.read()
    e_mail=request.forms.get("e_mail")
    lozinka=str(request.forms.get("lozinka"))
    svi_korisnici=procitaj_podatke_korisnik()
    for korisnik in svi_korisnici:
        if (korisnik._e_mail==e_mail):
            if (korisnik._lozinka==lozinka):
                trenutnikorisnik=korisnik._e_mail
                podaci=procitaj_podatke_tetovaze()
                return template('recenzije',data=podaci,template_lookup=[template_path])
            else:
                redirect ('/signup')
    redirect ('/signup')

@app.route('/signosoblje')
def sign_osoblje():
    return template('signin',data=None,form_akcija="provjerao",template_lookup=[template_path])

@app.route('/provjerao',method='POST')
def provjeraosoblja():
    global trenutnoosoblje
    postdata=request.body.read()
    e_mail=request.forms.get("e_mail")
    lozinka=str(request.forms.get("lozinka"))
    svo_osoblje=procitaj_podatke_osoblja()
    for osoblje in svo_osoblje:
        if (osoblje._e_mail==e_mail):
            if (osoblje._lozinka==lozinka):
                trenutnoosoblje=osoblje._ime_prezime
                tetovaze=procitaj_podatke_tetovaze()
                return template('tattoo',data=tetovaze,template_lookup=[template_path])
            else:
                redirect ('/signup')    
    redirect ('/signup')

@app.route('/signup')
def signup():
    return template("signup",data=None,form_akcija="/dodaj",template_lookup=[template_path])    

@app.route("/dodaj",method='POST')
def dodajkorisnika():
    global trenutnikorisnik
    postdata=request.body.read()
    e_mail=request.forms.get("e_mail")
    lozinka=str(request.forms.get("lozinka"))
    sacuvaj_korisnika(e_mail,lozinka)
    trenutnikorisnik = e_mail
    redirect('/recenzije')

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

    ime_prezime=request.forms.get("ime_prezime")
    datumpocetkarada=request.forms.get("datumpocetkarada")
    brojtetovazaizradenih=int(request.forms.get("brojtetovazaizradenih"))
    e_mail=request.forms.get("e_mail")
    lozinka=str(request.forms.get("lozinka"))
    sacuvaj_novo_osoblje(ime_prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka)

    redirect('/osoblje')

@app.route('/azuriraj-osoblje')
def azuriraj_osoblje_():
    osoblje_id=request.query['osobljeid']
    osoblje=dohvati_osoblje_po_id(osoblje_id)
    return template('formaosoblje',data=osoblje, form_akcija="/azuriraj-osoblje-save",template_lookup=[template_path])

@app.route('/azuriraj-osoblje-save',method='POST')
def azuriraj_osoblje_save():
    osoblje_id=request.forms.get("osobljeid")
    ime_prezime=request.forms.get("ime_prezime")
    datumpocetkarada=request.forms.get("datumpocetkarada")
    brojtetovazaizradenih=int(request.forms.get("brojtetovazaizradenih"))
    e_mail=request.forms.get("e_mail")
    lozinka=str(request.forms.get("lozinka"))

    azuriraj_osoblje(osoblje_id,ime_prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka)
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
    listaosoblja = svo_osoblje()
    listatetovaza = sve_tetovaze()
    return template('formaracuni',data=None, podaciO=listaosoblja, podaciT=listatetovaza,form_akcija="/spremi-racun",template_lookup=[template_path])

@app.route('/spremi-racun', method='POST')
def spremi_racun_():
    postdata=request.body.read()

    datum=request.forms.get("datum")
    osoblje=request.forms.get("osoblje")
    tetovaze=request.forms.get("tetovaze")
    ukupno=int(request.forms.get("ukupno"))
    sacuvaj_novi_racun(datum,osoblje,tetovaze,ukupno)

    redirect('/racuni')

@app.route('/azuriraj-racun')
def azuriraj_racun_():
    racuni_id=request.query['racuniid']
    racuni=dohvati_racun_po_id(racuni_id)
    listaosoblja = svo_osoblje()
    listatetovaza = sve_tetovaze()
    return template('formaracuni',data=racuni, podaciO=listaosoblja, podaciT=listatetovaza, form_akcija="/azuriraj-racun-save",template_lookup=[template_path])

@app.route('/azuriraj-racun-save',method='POST')
def azuriraj_racun_save():
    racuni_id=request.forms.get("racuniid")
    datum=request.forms.get("datum")
    osoba=request.forms.get("osoblje")
    tetovaze=request.forms.get("tetovaze")
    ukupno=int(request.forms.get("ukupno"))

    azuriraj_racun(racuni_id,datum,osoba,tetovaze,ukupno)
    redirect('/racuni')

@app.route('/izbrisi-racun')
def izbrisi_racun_():
    racuni_id = request.query['racuniid']
    izbrisi_racun(racuni_id)
    redirect('/racuni')

@app.route('/tetovaze')
def tetovaze_():
    podaci=procitaj_podatke_tetovaze()
    return template('tetovaze', data=podaci, template_lookup=[template_path])

@app.route('/velika')
def velika_tetovaza_():
    podaci=velika_tetovaza()
    return template('tetovaze',data=podaci,template_lookup=[template_path])

@app.route('/mala')
def mala_tetovaza_():
    podaci=mala_tetovaza()
    return template('tetovaze',data=podaci,template_lookup=[template_path])
        
@app.route('/recenzije')
def recenzije_():
    podaci=procitaj_podatke_tetovaze()
    return template('recenzije', data=podaci, template_lookup=[template_path])

@app.route('/formarecenzije')
def formarecenzije():
    podaci=procitaj_recenzije

@app.route('/odmanje')
def od_manje():
    podaci=odmanje()
    return template('tetovaze',data=podaci,template_lookup=[template_path])

@app.route('/odvece')
def od_vece():
    podaci=odvece()
    return template('tetovaze',data=podaci,template_lookup=[template_path])

@app.route('/formarecenzije')
def urediocjenu():
    return template("formarecenzije",data=None,template_lookup=[template_path])

@app.route('/odjava')
def odjava():
    global trenutnikorisnik, trenutnoosoblje
    trenutnikorisnik=""
    trenutnoosoblje=""
    redirect('/')

run(app, host='localhost', port = 1212)
