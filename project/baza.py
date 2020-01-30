import sqlite3
import os,sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from tetovaze import Tetovaze 
from osoblje import Osoblje
from racuni import Racuni
from korisnik import Korisnik

def unesi_demo_podatke():
    con=sqlite3.connect('tattoo.db')
    try:
        cur=con.cursor()
        cur.executescript("""
        
        DROP TABLE IF EXISTS tattoo;
        DROP TABLE IF EXISTS osoblje;
        DROP TABLE IF EXISTS racuni;
        DROP TABLE IF EXISTS korisnik;
        DROP TABLE IF EXISTS tetovaze;
        
        CREATE TABLE tetovaze (
            id INTEGER PRIMARY KEY,
            naziv text NOT NULL,
            velicina text NOT NULL,
            vrijeme time NOT NULL,
            cijena integer NOT NULL);
        """)
        print("Uspjesno kreirana tablica tetovaze")

        cur.execute("INSERT INTO tetovaze (naziv,velicina,vrijeme,cijena) VALUES (?,?,?,?)",("Ptica","mala",60,500))
        cur.execute("INSERT INTO tetovaze (naziv,velicina,vrijeme,cijena) VALUES (?,?,?,?)",("Zmaj","velika",180,5000))
        con.commit()

        print("Uspjesno uneseni testni podaci u tablicu tetovaze")

    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()


    # za tablicu osoblje
    try:
        cur=con.cursor()
        cur.executescript("""
        
        DROP TABLE IF EXISTS osoblje;
        
        CREATE TABLE osoblje (
            id INTEGER PRIMARY KEY,
            ime text NOT NULL,
            prezime text NOT NULL,
            datumpocetkarada date NOT NULL,
            brojtetovazaizradenih integer NOT NULL);
        """)
        print("Uspjesno kreirana tablica osoblje")

        cur.execute("INSERT INTO osoblje (ime,prezime,datumpocetkarada,brojtetovazaizradenih) VALUES (?,?,?,?)",("Ivana","Konta","2020-01-01",4))
        cur.execute("INSERT INTO osoblje (ime,prezime,datumpocetkarada,brojtetovazaizradenih) VALUES (?,?,?,?)",("Dorotea","Bertović","2019-12-07",7))
        con.commit()

        print("Uspjesno uneseni testni podaci u tablicu osoblje")

    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()

    # tablica racuni
    try:
        cur=con.cursor()
        cur.executescript("""
        
        DROP TABLE IF EXISTS racun;
        DROP TABLE IF EXISTS racuni;
        
        CREATE TABLE racuni (
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

        #tablica korisnik
    try:
        cur=con.cursor()
        cur.executescript("""
        
        DROP TABLE IF EXISTS korisnik;
        
        CREATE TABLE korisnik (
        id INTEGER PRIMARY KEY,
        e_mail email NOT NULL,
        lozinka password NOT NULL);
        """)
        print("Uspjesno kreirana tablica korisnik")

        cur.execute("INSERT INTO korisnik (e_mail, lozinka) VALUES (?,?)", ("ikonta@pmfst.hr","ikonta"))
        cur.execute("INSERT INTO korisnik (e_mail, lozinka) VALUES (?,?)", ("dbertovic@pmfst.hr","dbertovic"))
        con.commit()

        print("Uspjesno uneseni testni podaci u tablicu korisnik")


    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()

    con.close()

def procitaj_podatke_tetovaze():
    con=sqlite3.connect("tattoo.db")
    lista_tetovaza=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT id,naziv,velicina,vrijeme,cijena FROM tetovaze """)
        
        podaci=cur.fetchall()

        for tat in podaci:
            # 0 - id
            # 1 - naziv
            # 2 - velicina
            # 3 - vrijeme
            # 4 - cijena

            t=Tetovaze(tat[0],tat[1],tat[2],tat[3],tat[4])
            lista_tetovaza.append(t)

        print ("Uspjesno dohvaceni svi podaci iz tablice tetovaze")

        for t in lista_tetovaza:
            print(t)
        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice tetovaze: ",e)
        con.rollback()

    con.close()
    return lista_tetovaza

def sacuvaj_novu_tetovazu(naziv,velicina,vrijeme,cijena):
    con=sqlite3.connect("tattoo.db")
    try:
        cur=con.cursor()
        cur.execute("INSERT INTO tetovaze (naziv,velicina,vrijeme,cijena) VALUES (?,?,?,?)",(naziv,velicina,vrijeme,cijena))
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
        cur.execute("SELECT id, naziv, velicina, vrijeme, cijena FROM tetovaze WHERE id=?", (tetovaze_id))
        podaci = cur.fetchone()

        print ("podaci", podaci)
        tetovaze = Tetovaze(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4])

        print("Uspjesno dohvacena tetovaza iz baze podataka po ID-u")

    except Exception as e:
        print ("Dogodila se greska pri dohvacanju tetovaze iz baze podataka po ID-u: ", e)
        con.rollback()

    con.close()
    return tetovaze  

def azuriraj_tetovazu(tetovaze_id, naziv, velicina, vrijeme, cijena):
    con = sqlite3.connect("tattoo.db")
    try:

        cur = con.cursor()
        cur.execute("UPDATE tetovaze SET naziv = ?, velicina = ?, vrijeme = ?, cijena = ? WHERE id = ?", (naziv, velicina, vrijeme, cijena, tetovaze_id))
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
        cur.execute(""" SELECT id,ime,prezime,datumpocetkarada,brojtetovazaizradenih FROM osoblje """)
        
        podaci=cur.fetchall()

        for osob in podaci:
            # 0 - id
            # 1 - ime
            # 2 - prezime
            # 3 - datum
            # 4 - broj

            o=Osoblje(osob[0],osob[1],osob[2],osob[3],osob[4])
            lista_osoblja.append(o)

        print ("Uspjesno dohvaceni svi podaci iz tablice osoblja")

        for o in lista_osoblja:
            print(o)
        
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice osoblja: ",e)
        con.rollback()

    con.close()
    return lista_osoblja

def sacuvaj_novo_osoblje(ime,prezime,datumpocetkarada,brojtetovazaizradenih):
    con=sqlite3.connect("tattoo.db")
    try:
        cur=con.cursor()
        cur.execute("INSERT INTO osoblje (ime,prezime,datumpocetkarada,brojtetovazaizradenih) VALUES (?,?,?,?)",(ime,prezime,datumpocetkarada,brojtetovazaizradenih))
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
        cur.execute("SELECT id, ime, prezime, datumpocetkarada, brojtetovazaizradenih FROM osoblje WHERE id=?", (osoblje_id))
        podaci = cur.fetchone()

        print ("podaci", podaci)
        osoblje = Osoblje(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4])

        print("Uspjesno dohvaceno osoblje iz baze podataka po ID-u")

    except Exception as e:
        print ("Dogodila se greska pri dohvacanju osoblja iz baze podataka po ID-u: ", e)
        con.rollback()

    con.close()
    return osoblje  

def azuriraj_osoblje(osoblje_id, ime, prezime, datumpocetkarada, brojtetovazaizradenih):
    con = sqlite3.connect("tattoo.db")
    try:

        cur = con.cursor()
        cur.execute("UPDATE osoblje SET ime = ?, prezime = ?, datumpocetkarada = ?, brojtetovazaizradenih = ? WHERE id = ?", (ime, prezime, datumpocetkarada, brojtetovazaizradenih, osoblje_id))
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
