import sqlite3
import os,sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

from tattoo import Tattoo 

def unesi_demo_podatke():
    con=sqlite3.connect('tattoo.db')
    try:
        cur=con.cursor()
        cur.execute("DROP TABLE IF EXISTS tattoo")

        cur.execute("CREATE TABLE tattoo (tattoo_id INTEGER PRIMARY KEY AUTOINCREMENT, naziv TEXT NOT NULL, velicina TEXT NOT NULL, vrijeme TIME NOT NULL, cijena INTEGER NOT NULL)")
        cur.execute("CREATE TABLE osoblje (osoblje_id INTEGER PRIMARY KEY AUTOINCREMENT, ime TEXT NOT NULL, prezime TEXT NOT NULL)")
        cur.execute("CREATE TABLE racun (racun_id INTEGER PRIMARY KEY AUTOINCREMENT, broj_racuna INTEGER NOT NULL, osoblje_id INTEGER NOT NULL, tattoo_id INTEGER NOT NULL, ukupno INTEGER NOT NULL)")

        cur.execute("INSERT INTO tattoo (naziv,velicina,vrijeme,cijena) VALUES (?,?,?)",("Ptica","mala",60,500))
        con.commit()
        cur.execute("INSERT INTO osoblje (ime,prezime) VALUES (?,?)",("Ivana","Konta"))
        con.commit()

    except Exception as e:
        print("Dogodila se greska pri kreiranju demo podataka: ",e)
        con.rollback()
    con.close()

def procitaj_podatke():
    con=sqlite3.connect("tattoo.db")
    lista_tetovaza=[]
    try:
        cur=con.cursor()
        cur.execute(""" SELECT tattoo_id,naziv,velicina,vrijeme,cijena FROM tattoo """)
        
        podaci=cur.fetchall()

        for tat in podaci:
            # 0 - id
            # 1 - naziv
            # 2 - velicina
            # 3 - vrijeme
            # 4 - cijena

            t=Tattoo(tat[0],tat[1],tat[2],tat[3],tat[4])
            lista_tetovaza.append(t)

        print ("Uspjesno dohvaceni svi podaci iz tablice tetovaza")

        for t in lista_tetovaza:
            print(t)
        
    
    except Exception as e:
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice tetovaza: ",e)
        con.rollback()

    con.close()
    return lista_tetovaza

def sacuvaj_novu_tetovazu(naziv,velicina,vrijeme,cijena):
    con=sqlite3.connect("tattoo.db")
    try:
        cur=con.cursor()
        cur.execute("INSERT INTO tattoo (naziv,velicina,vrijeme,cijena) VALUES (?,?,?,?)",(naziv,velicina,vrijeme,cijena))
        con.commit()

        print("Uspjesno dodan novi profesor u bazu podataka")
    
    except Exception as e:
        print("Dogodila se greska pri dodavanju novog profesora u bazu podataka: ",e)
        con.rollback()

    con.close()
