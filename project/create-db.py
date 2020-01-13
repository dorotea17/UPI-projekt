import sqlite3 as lite
import sys

con=lite.connect('data\\tattoo.db')

print("Creating database/tables...")
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS tattoo")

    cur.execute("CREATE TABLE tattoo (id INTEGER PRIMARY KEY AUTOINCREMENT, tattoo_id TEXT, title TEXT, velicina TEXT, vrijeme TIME, cijena INTEGER)")

    cur.execute("CREATE TABLE osoblje (id INTEGER PRIMARY KEY AUTOINCREMENT, osoblje_id TEXT, ime TEXT, prezime TEXT)")

    cur.execute("CREATE TABLE racun (id INTEGER PRIMARY KEY AUTOINCREMENT, racun_id TEXT, broj_racuna INTEGER, osoblje_id TEXT, ukupno INTEGER)")

con.close()
print("Database/tables created.")
