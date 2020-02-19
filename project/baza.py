import sqlite3
import os,sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from tetovaze import Tetovaze 
from osoblje import Osoblje
from racuni import Racuni
from korisnik import Korisnik
from recenzije import Recenzije

def unesi_demo_podatke():
    con=sqlite3.connect('tattoo.db')
    try:
        cur=con.cursor()
        cur.executescript("""
        
        DROP TABLE IF EXISTS tetovaze;
        CREATE TABLE IF NOT EXISTS tetovaze (
            id INTEGER PRIMARY KEY,
            link text NOT NULL,
            naziv text NOT NULL,
            velicina text NOT NULL,
            vrijeme time NOT NULL,
            cijena integer NOT NULL);
        """)
        print("Uspjesno kreirana tablica tetovaze")

        cur.execute("INSERT INTO tetovaze (link,naziv,velicina,vrijeme,cijena) VALUES (?,?,?,?,?)",("https://i.pinimg.com/originals/85/75/53/8575531fb4d85fdd604f72f391f5f4d4.jpg","Ptica","mala",60,500))
        cur.execute("INSERT INTO tetovaze (link,naziv,velicina,vrijeme,cijena) VALUES (?,?,?,?,?)",("https://parryz.com/wp-content/uploads/2017/08/Awesome-Simple-Dragon-Tattoo.jpg","Zmaj","velika",180,5000))
        con.commit()

        print("Uspjesno uneseni testni podaci u tablicu tetovaze")

    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()

        #tablica korisnik
    try:
        cur=con.cursor()
        cur.executescript("""
                
        DROP TABLE IF EXISTS korisnik;
        CREATE TABLE IF NOT EXISTS korisnik (
        id INTEGER PRIMARY KEY,
        e_mail email NOT NULL,
        lozinka password NOT NULL);
        """)
        print("Uspjesno kreirana tablica korisnik")

        cur.execute("INSERT INTO korisnik (e_mail, lozinka) VALUES (?,?)", ("korisnik@pmfst.hr","korisnik"))
        con.commit()

        print("Uspjesno uneseni testni podaci u tablicu korisnik")


    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()


    # za tablicu osoblje
    try:
        cur=con.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS osoblje;        
        CREATE TABLE IF NOT EXISTS osoblje (
        id INTEGER PRIMARY KEY,
        ime text NOT NULL,
        prezime text NOT NULL,
        datumpocetkarada date NOT NULL,
        brojtetovazaizradenih integer NOT NULL,
        e_mail email NOT NULL,
        lozinka password NOT NULL);
        """)
        print("Uspjesno kreirana tablica osoblje")

        cur.execute("INSERT INTO osoblje (ime,prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka) VALUES (?,?,?,?,?,?)",("Ivana","Konta","2020-01-01",4,"ikonta@pmfst.hr","ikonta"))
        cur.execute("INSERT INTO osoblje (ime,prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka) VALUES (?,?,?,?,?,?)",("Dorotea","Bertović","2019-12-07",7,"dbertovic@pmfst.hr","dbertovic"))
        con.commit()

        print("Uspjesno uneseni testni podaci u tablicu osoblje")

    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()

    # tablica racuni
    try:
        cur=con.cursor()
        cur.executescript("""
        
        DROP TABLE IF EXISTS racuni;
        CREATE TABLE IF NOT EXISTS racuni (
            id INTEGER PRIMARY KEY,
            datum date NOT NULL,
            osoblje_id integer NOT NULL,
            tetovaze_id integer NOT NULL,
            ukupno integer NOT NULL,
            FOREIGN KEY (osoblje_id) REFERENCES osoblje (id),
            FOREIGN KEY (tetovaze_id) REFERENCES tetovaze (id));
            
        """)
        print("Uspjesno kreirana tablica racuni")
        
        cur.execute("INSERT INTO racuni (datum, osoblje_id, tetovaze_id, ukupno) VALUES (?,?,?,?)", ("2019-12-12",2,2,5000))
        cur.execute("INSERT INTO racuni (datum, osoblje_id, tetovaze_id, ukupno) VALUES (?,?,?,?)", ("2020-01-01",1,1,500))
        con.commit()

        print("Uspjesno uneseni testni podaci u tablicu racuni")


    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()

        #recenzije
    try:
        cur=con.cursor()
        cur.executescript("""
                
        DROP TABLE IF EXISTS recenzije;
        CREATE TABLE IF NOT EXISTS recenzije (
        ocjena INTEGER NOT NULL,
        tetovaze_id integer NOT NULL,
        korisnik_id integer NOT NULL,
        FOREIGN KEY (tetovaze_id) REFERENCES tetovaze (id),
        FOREIGN KEY (korisnik_id) REFERENCES korisnik (id));
        """)
        print("Uspjesno kreirana tablica recenzije")

    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()
    con.close()

def procitaj_recenzije():
    con=sqlite3.connect('tattoo.db')
    lista_recenzija=[]
    try:
        cur=con.cursor()
        cur.execute("SELECT ocjena, tetovaze_id, korisnik_id FROM recenzije")
        podaci=cur.fetchall()

        for rec in podaci:
            r=Recenzije(rec[0],rec[1],rec[2])
            lista_recenzija.append(r)
        
        print("Uspjesno dohvaceni svi podaci iz tablice recenzije")

    except Exception as e:
        print("Dogodila se greska pri dohvacanju podataka iz tablice recenzije: ",e)
        con.rollback()
    con.close()

def procitaj_podatke_tetovaze():
    con=sqlite3.connect("tattoo.db")
    lista_tetovaza=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT id,link,naziv,velicina,vrijeme,cijena FROM tetovaze """)
        
        podaci=cur.fetchall()

        for tat in podaci:
            # 0 - id
            # 1 - link
            # 2 - naziv
            # 3 - velicina
            # 4 - vrijeme
            # 5 - cijena

            t=Tetovaze(tat[0],tat[1],tat[2],tat[3],tat[4],tat[5])
            lista_tetovaza.append(t)

        print ("Uspjesno dohvaceni svi podaci iz tablice tetovaze")

        for t in lista_tetovaza:
            print(t)
        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice tetovaze: ",e)
        con.rollback()

    con.close()
    return lista_tetovaza

def sacuvaj_novu_tetovazu(link,naziv,velicina,vrijeme,cijena):
    con=sqlite3.connect("tattoo.db")
    try:
        cur=con.cursor()
        cur.execute("INSERT INTO tetovaze (link,naziv,velicina,vrijeme,cijena) VALUES (?,?,?,?,?)",(link,naziv,velicina,vrijeme,cijena))
        con.commit()

        print("Uspjesno dodana nova tetovaza u bazu podataka")
    
    except Exception as e:
        print("Dogodila se greska pri dodavanju nove tetovaze u bazu podataka: ",e)
        con.rollback()

    con.close()
 
def izbrisi_tetovazu(tetovaze_id):
    con = sqlite3.connect("tattoo.db")
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM tetovaze WHERE id=?;", (tetovaze_id))
        con.commit()

        print ("uspjesno izbrisana tetovaza iz baze podataka")

    except Exception as e:
        print ("Dogodila se greska pri brisanju tetovaze iz baze podaraka: ", e)
        con.rollback()

    con.close()

def dohvati_tetovazu_po_id(tetovaze_id):
    con = sqlite3.connect("tattoo.db")
    tetovaze = None
    try:

        cur = con.cursor()
        cur.execute("SELECT id, link, naziv, velicina, vrijeme, cijena FROM tetovaze WHERE id=?", (tetovaze_id))
        podaci = cur.fetchone()

        print ("podaci", podaci)
        tetovaze = Tetovaze(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4],podaci[5])

        print("Uspjesno dohvacena tetovaza iz baze podataka po ID-u")

    except Exception as e:
        print ("Dogodila se greska pri dohvacanju tetovaze iz baze podataka po ID-u: ", e)
        con.rollback()

    con.close()
    return tetovaze  

def trazitetovazu(tetovaze_naziv):
    con = sqlite3.connect("tattoo.db")
    tetovaze = None
    try:

        cur = con.cursor()
        cur.execute("SELECT id, link, naziv, velicina, vrijeme, cijena FROM tetovaze WHERE naziv=?", (tetovaze_naziv))
        podaci = cur.fetchone()

        print ("podaci", podaci)
        tetovaze = Tetovaze(podaci[0])
        print("Uspjesno dohvacena tetovaza iz baze podataka po nazivu")

    except Exception as e:
        print ("Dogodila se greska pri dohvacanju tetovaze iz baze podataka po nazivu: ", e)
        con.rollback()

    con.close()
    return tetovaze  


def azuriraj_tetovazu(tetovaze_id, link, naziv, velicina, vrijeme, cijena):
    con = sqlite3.connect("tattoo.db")
    try:

        cur = con.cursor()
        cur.execute("UPDATE tetovaze SET link = ?, naziv = ?, velicina = ?, vrijeme = ?, cijena = ? WHERE id = ?", (link, naziv, velicina, vrijeme, cijena, tetovaze_id))
        con.commit()

        print("uspjesno ažurirana tetovaza iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju tetovaze iz baze podataka: ", e)
        con.rollback()

    con.close()

def procitaj_podatke_osoblja():
    con=sqlite3.connect("tattoo.db")
    lista_osoblja=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT id,ime,prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka FROM osoblje """)
        
        podaci=cur.fetchall()

        for osob in podaci:
            # 0 - id
            # 1 - ime
            # 2 - prezime
            # 3 - datum
            # 4 - broj
            # 5 - e_mail
            # 6 - lozinka

            o=Osoblje(osob[0],osob[1],osob[2],osob[3],osob[4],osob[5],osob[6])
            lista_osoblja.append(o)

        print ("Uspjesno dohvaceni svi podaci iz tablice osoblja")

        for o in lista_osoblja:
            print(o)
        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice osoblja: ",e)
        con.rollback()

    con.close()
    return lista_osoblja

def sacuvaj_novo_osoblje(ime,prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka):
    con=sqlite3.connect("tattoo.db")
    try:
        cur=con.cursor()
        cur.execute("INSERT INTO osoblje (ime,prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka) VALUES (?,?,?,?,?,?)",(ime,prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka))
        con.commit()

        print("Uspjesno dodano novo osoblje u bazu podataka")
    
    except Exception as e:
        print("Dogodila se greska pri dodavanju novog osoblja u bazu podataka: ",e)
        con.rollback()

    con.close()
 
def izbrisi_osoblje(osoblje_id):
    con = sqlite3.connect("tattoo.db")
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM osoblje WHERE id=?;", (osoblje_id))
        con.commit()

        print ("uspjesno izbrisano osoblje iz baze podataka")

    except Exception as e:
        print ("Dogodila se greska pri brisanju osoblja iz baze podataka: ", e)
        con.rollback()

    con.close()

def dohvati_osoblje_po_id(osoblje_id):
    con = sqlite3.connect("tattoo.db")
    osoblje = None
    try:

        cur = con.cursor()
        cur.execute("SELECT id, ime, prezime, datumpocetkarada, brojtetovazaizradenih, e_mail, lozinka FROM osoblje WHERE id=?", (osoblje_id))
        podaci = cur.fetchone()

        print ("podaci", podaci)
        osoblje = Osoblje(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4], podaci[5], podaci[6])

        print("Uspjesno dohvaceno osoblje iz baze podataka po ID-u")

    except Exception as e:
        print ("Dogodila se greska pri dohvacanju osoblja iz baze podataka po ID-u: ", e)
        con.rollback()

    con.close()
    return osoblje  

def azuriraj_osoblje(osoblje_id, ime, prezime, datumpocetkarada, brojtetovazaizradenih, e_mail, lozinka):
    con = sqlite3.connect("tattoo.db")
    try:

        cur = con.cursor()
        cur.execute("UPDATE osoblje SET ime = ?, prezime = ?, datumpocetkarada = ?, brojtetovazaizradenih = ?, e_mail = ?, lozinka = ? WHERE id = ?", (ime, prezime, datumpocetkarada, brojtetovazaizradenih, e_mail, lozinka, osoblje_id))
        con.commit()

        print("uspjesno ažurirano osoblje iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju osoblja iz baze podataka: ", e)
        con.rollback()

    con.close()

def procitaj_podatke_korisnik():
    con=sqlite3.connect("tattoo.db")
    lista_korisnika=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT id,e_mail,lozinka FROM korisnik """)
    
        podaci=cur.fetchall()

        for kor in podaci:
            # 0 - id
            # 1 - e_mail
            # 2 - lozinka

            k=Korisnik(kor[0],kor[1],kor[2])
            lista_korisnika.append(k)

        print ("Uspjesno dohvaceni svi podaci iz tablice korisnika")

        for k in lista_korisnika:
            print(k)
        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice korisnika: ",e)
        con.rollback()

    con.close()
    return lista_korisnika

def procitaj_podatke_racuna():
    con=sqlite3.connect("tattoo.db")
    lista_racuna=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT * FROM tetovaze INNER JOIN racuni
                        ON racuni.tetovaze_id = tetovaze.id INNER JOIN osoblje
                        ON racuni.osoblje_id = osoblje.id """)
        
        podaci=cur.fetchall()

        for e in podaci:
            lista = []
            lista.append(Tetovaze(e[0],e[1],e[2],e[3],e[4],e[5]))
            lista.append(Racuni(e[6],e[7],e[8],e[9],e[10]))
            lista.append(Osoblje(e[11],e[12],e[13],e[14],e[15],e[16],e[17]))
            lista_racuna.append(lista)


        print ("Uspjesno dohvaceni svi podaci iz tablice racuna")

        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice racuna: ",e)
        con.rollback()

    con.close()
    return lista_racuna

def sacuvaj_novi_racun(datum,osoba,tetovaza,ukupno):
    con=sqlite3.connect("tattoo.db")
    try:
        cur=con.cursor()
        imena=osoba.split(" ")
        ime=imena[0]
        prezime=imena[1]
        cur.execute("SELECT id FROM osoblje WHERE ime = ? AND prezime = ? ",(ime,prezime))
        osoblje_id=cur.fetchone()
        osoblje_id=osoblje_id[0]

        cur.execute("SELECT id FROM tetovaze WHERE naziv = ?",(tetovaza))
        tetovaze_id=cur.fetchone()
        tetovaze_id=tetovaze_id[0]
        cur.execute("INSERT INTO racuni (datum,osoblje_id,tetovaze_id,ukupno) VALUES (?,?,?,?)",(datum,osoblje_id,tetovaze_id,ukupno))
        con.commit()

        print("Uspjesno dodan novi racun u bazu podataka")
    
    except Exception as e:
        print("Dogodila se greska pri dodavanju novog racuna u bazu podataka: ",e)
        con.rollback()

    con.close()
 
def izbrisi_racun(racuni_id):
    con = sqlite3.connect("tattoo.db")
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM racuni WHERE id=?;", (racuni_id))
        con.commit()

        print ("uspjesno izbrisan racun iz baze podataka")

    except Exception as e:
        print ("Dogodila se greska pri brisanju racuna iz baze podataka: ", e)
        con.rollback()

    con.close()

def dohvati_racun_po_id(racuni_id):
    con = sqlite3.connect("tattoo.db")
    racuni = None
    try:
        cur = con.cursor()
        cur.execute("SELECT id, datum, osoblje_id, tetovaze_id, ukupno FROM racuni WHERE id=?", (racuni_id))
        podaci = cur.fetchone()

        # cur.execute("SELECT ime, prezime FROM osoblje WHERE id = ?",(podaci[2]))
        # osoba=cur.fetchone()
        # osoba=osoba[0]+" "+osoba[1]

        # cur.execute("SELECT naziv FROM tetovaze WHERE id = ?",(podaci[3]))
        # tetovaza=cur.fetchone()
        # tetovaza=tetovaza[0]

        print ("podaci", podaci)
        racuni = Racuni(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4])

        print("Uspjesno dohvacen racun iz baze podataka po ID-u")

    except Exception as e:
        print ("Dogodila se greska pri dohvacanju racuna iz baze podataka po ID-u: ", e)
        con.rollback()

    con.close()
    return racuni 

def azuriraj_racun(racuni_id, datum, osoba, tetovaza, ukupno):
    con = sqlite3.connect("tattoo.db")
    try:
        cur = con.cursor()
        imena=osoba.split(" ")
        ime=imena[0]
        prezime=imena[1]
        cur.execute("SELECT id FROM osoblje WHERE ime = ? AND prezime = ? ",(ime,prezime))
        osoblje_id=cur.fetchone()
        osoblje_id=osoblje_id[0]

        cur.execute("SELECT id FROM tetovaze WHERE naziv = ?",(tetovaza))
        tetovaze_id=cur.fetchone()
        tetovaze_id=tetovaze_id[0]
        cur.execute("UPDATE racuni SET datum = ?, osoblje_id = ?, tetovaze_id = ?, ukupno = ? WHERE id = ?", (datum, osoblje_id, tetovaze_id, ukupno, racuni_id))
        con.commit()

        print("uspjesno ažuriran racun iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju racuna iz baze podataka: ", e)
        con.rollback()

    con.close()

def velika_tetovaza():
    con=sqlite3.connect("tattoo.db")
    lista_velikih=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT id,link,naziv,velicina,vrijeme, cijena FROM tetovaze """)
        
        podaci=cur.fetchall()

        for tat in podaci:
            if (tat[3]=="velika"):
                t=Tetovaze(tat[0],tat[1],tat[2],tat[3],tat[4],tat[5])
                lista_velikih.append(t)

        print ("Uspjesno dohvaceni svi podaci iz tablice tetovaza")

        for t in lista_velikih:
            print(t)
        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice tetovaza: ",e)
        con.rollback()

    con.close()
    return lista_velikih

def mala_tetovaza():
    con=sqlite3.connect("tattoo.db")
    lista_malih=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT id,link,naziv,velicina,vrijeme, cijena FROM tetovaze """)
        
        podaci=cur.fetchall()

        for tat in podaci:
            if (tat[3]=="mala"):
                t=Tetovaze(tat[0],tat[1],tat[2],tat[3],tat[4],tat[5])
                lista_malih.append(t)

        print ("Uspjesno dohvaceni svi podaci iz tablice tetovaza")

        for t in lista_malih:
            print(t)
        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice tetovaza: ",e)
        con.rollback()

    con.close()
    return lista_malih

def odmanje():
    con=sqlite3.connect('tattoo.db')
    listaodmanje=[]
    try:
        cur=con.cursor()
        cur.execute("SELECT * FROM tetovaze ORDER BY cijena ASC")
        podaci=cur.fetchall()
        for tat in podaci: 
            t=Tetovaze(tat[0],tat[1],tat[2],tat[3],tat[4],tat[5])
            listaodmanje.append(t)

    except Exception as e:
        print("Pogreška u sortiranju: ",e)
        con.rollback()
    con.close()
    return listaodmanje

def odvece():
    con=sqlite3.connect('tattoo.db')
    listaodvece=[]
    try:
        cur=con.cursor()
        cur.execute("SELECT * FROM tetovaze ORDER BY cijena DESC")
        podaci=cur.fetchall()
        for tat in podaci: 
            t=Tetovaze(tat[0],tat[1],tat[2],tat[3],tat[4],tat[5])
            listaodvece.append(t)
             

    except Exception as e:
        print("Pogreška u sortiranju: ",e)
        con.rollback()
    con.close()
    return listaodvece

def sacuvaj_korisnika(e_mail,lozinka):
    con=sqlite3.connect('tattoo.db')
    try:
        cur=con.cursor()
        cur.execute("INSERT INTO korisnik (e_mail,lozinka) VALUES (?,?)",(e_mail,lozinka))
        con.commit()

        print("Uspjesno dodan novi korisnik u bazu podataka")
    
    except Exception as e:
        print("Dogodila se greska pri dodavanju novog korisnika u bazu podataka: ",e)
        con.rollback()

    con.close()

def traziosoblje(osoblje_ime):
    con=sqlite3.connect('tattoo.db')
    osoblje=None
    try:
        cur=con.cursor()
        cur.execute("SELECT id, ime, prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka FROM osoblje WHERE ime=?", (osoblje_ime))
        podaci = cur.fetchone()

        print ("podaci", podaci)
        osoblje = Osoblje(podaci[0])

    except Exception as e:
        print("Dogodila se greska pri dodavanju novog korisnika u bazu podataka: ",e)
        con.rollback()

    con.close()
    return osoblje

def svo_osoblje():
    con=sqlite3.connect('tattoo.db')
    listaosoblja=[]
    try:
        cur = con.cursor()
        cur.execute("SELECT ime, prezime FROM osoblje")
        osobe=cur.fetchall()
        for o in osobe:
            listaosoblja.append(o[0]+" "+ o[1])
    except Exception as e:
        print ("Dogodila se greška pri čitanju podataka: ",e)
        con.rollback()
    con.close()
    return listaosoblja

def sve_tetovaze():
    con=sqlite3.connect('tattoo.db')
    listatetovaza=[]
    try:
        cur=con.cursor()
        cur.execute("SELECT naziv FROM tetovaze")
        tetovaze=cur.fetchall()
        for t in tetovaze:
            listatetovaza.append(t[0])
    except Exception as e:
        print("Dogodila se greska pri citanju podataka: ",e)
        con.rollback()
    con.close()
    return listatetovaza
