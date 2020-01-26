import sqlite3
import os,sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from tattoo import Tattoo 
# from osoblje import Osoblje
# from racuni import Racuni

def unesi_demo_podatke():
    con=sqlite3.connect('tattoo.db')
    #za tablicu tetovaze
    try:
        cur=con.cursor()
        cur.executescript("""
        
        DROP TABLE IF EXISTS tetovaze;
        
        CREATE TABLE tetovaze (
            id INTEGER PRIMARY KEY,
            naziv text NOT NULL,
            velicina text NOT NULL,
            vrijeme time NOT NULL,
            cijena integer NOT NULL);
        """)
        print("Uspjesno kreirana tablica tattoo")

        cur.execute("INSERT INTO tetovaze (naziv,velicina,vrijeme,cijena) VALUES (?,?,?)",("Ptica","mala",60,500))
        cur.execute("INSERT INTO tetovaze (naziv,velicina,vrijeme,cijena) VALUES (?,?,?)",("Zmaj","velika",180,5000))
        con.commit()

        print("Uspjesno uneseni testni podaci u tablicu tetovaze")

    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()

    # # za tablicu osoblje
    # try:
    #     cur=con.cursor()
    #     cur.executescript("""
        
    #     DROP TABLE IF EXISTS osoblje;
        
    #     CREATE TABLE osoblje (
    #         id INTEGER PRIMARY KEY,
    #         ime text NOT NULL,
    #         prezime text NOT NULL
    #         datumpocetkarada date NOT NULL
    #         brojtetovazaizradenih integer NOT NULL);
    #     """)
    #     print("Uspjesno kreirana tablica osoblje")

    #     cur.execute("INSERT INTO osoblje (ime,prezime,datumpocetkarada,brojtetovazaizradenih) VALUES (?,?,?,?)",("Ivana","Konta","2020-01-01"))
    #     cur.execute("INSERT INTO osoblje (ime,prezime,datumpocetkarada,brojtetovazaizradenih) VALUES (?,?,?,?)",("Dorotea","Bertović","2019-12-07"))
    #     con.commit()

    # except Exception as e:
    #     print("Dogodila se greska pri kreiranju demo podataka: ",e)
    #     con.rollback()

    # #tablica racuni
    #  try:
    #     cur=con.cursor()
    #     cur.executescript("""
        
    #     DROP TABLE IF EXISTS racuni;
        
    #     CREATE TABLE racuni (
    #         id INTEGER PRIMARY KEY,
    #         datum date NOT NULL,
    #         FOREIGN KEY (osoblje_id) REFERENCES osoblje (id),
    #         FOREIGN KEY (tattoo_id) REFERENCES tattoo (id),
    #         ukupno integer NOT NULL);
    #     """)
    #     print("Uspjesno kreirana tablica racuni")

    #     cur.execute("INSERT INTO racuni (datum, osoblje_id, tattoo_id, ukupno) VALUES (?,?,?,?)", ("2019-12-12",2,2,5000))
    #     cur.execute("INSERT INTO racuni (datum, osoblje_id, tattoo_id, ukupno) VALUES (?,?,?,?)", ("2020-01-01",1,1,500))
    #     con.commit()

    # except Exception as e:
    #     print("Dogodila se greska pri kreiranju demo podataka: ",e)
    #     con.rollback()

    #     #tablica korisnik
    #  try:
    #     cur=con.cursor()
    #     cur.executescript("""
        
    #     DROP TABLE IF EXISTS korisnik;
        
    #     CREATE TABLE korisnik (
    #     e-mail email NOT NULL,
    #     lozinka password NOT NULL);
    #     """)
    #     print("Uspjesno kreirana tablica korisnik")

    #     cur.execute("INSERT INTO korisnik (e-mail, lozinka) VALUES (?,?)", ("ikonta@pmfst.hr","ikonta"))
    #     cur.execute("INSERT INTO korisnik (e-mail, lozinka) VALUES (?,?)", ("dbertovic@pmfst.hr","dbertovic"))
    #     con.commit()

    # except Exception as e:
    #     print("Dogodila se greska pri kreiranju demo podataka: ",e)
    #     con.rollback()

    # con.close()

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

            t=Tattoo(tat[0],tat[1],tat[2],tat[3],tat[4])
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
 
 def izbrisi_tetovazu(tat_id):
     con = sqlite3.connect("tattoo.db")
     try:
         cur = con.cursor()
         cur.execute("DELETE FROM tetovaze WHERE id=?;", (tat_id))
         con.commit()

         print ("uspjesno izbrisana tetovaza iz baze podataka")

     except Exception as e:
         print ("Dogodila se greska pri brisanju tetovaze iz baze podaraka: ", e)
         con.rollback()

     con.close()

 def dohvati_tetovazu_po_id(tat_id):
     con = sqlite3.connect("tattoo.db")
     tattoo = None
     try:

         cur = con.cursor()
         cur.execute("SELECT id, naziv, velicina, vrijeme, cijena FROM tetovaze WHERE id=?", (tat_id))
         podaci = cur.fetchone()

         print ("podaci", podaci)
         tattoo = Tattoo(podaci[0], podaci[1], podaci[2], podaci[3], podaci[4])

         print("Uspjesno dohvacena tetovaza iz baze podataka po ID-u")

     except Exception as e:
         print ("Dogodila se greska pri dohvacanju tetovaze iz baze podataka po ID-u: ", e)
         con.rollback()

     con.close()
     return tattoo  

 def azuriraj_tetovazu(tat_id, naziv, velicina, vrijeme, cijena):
    con = sqlite3.connect("tattoo.db")
    try:

        cur = con.cursor()
        cur.execute("UPDATE tetovaze SET naziv = ?, velicina = ?, vrijeme = ?, cijena = ? WHERE id = ?", (naziv, velicina, vrijeme, cijena, tat_id))
        con.commit()

        print("uspjesno ažurirana tetovaza iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju tetovaze iz baze podataka: ", e)
        con.rollback()

    con.close()