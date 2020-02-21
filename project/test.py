import unittest
import os,sys,sqlite3,datetime

from baza import *
dirname=os.path.dirname(sys.argv[0])
from korisnik import korisnik

class TestStringMethods(unittest.TestCase):

    def test_init_mail_error(self):
        with self.assertRaises(ValueError):
            Korisnik("db@","")

    def test_init_password_error(self):
        with self.assertRaises(ValueError):
            Korisnik("","123")

    def test_init_sacuvaj_novi_racun(self):
        lista_unos=["2020-01-01","Ivana Konta","Ptica",500]
        sacuvaj_novi_racun(lista_unos[0],lista_unos[1],lista_unos[2],lista_unos[3])

        p=procitaj_podatke_racuna()
        i=len(p)-1
        lista_rezultat = [p[i][0]._ime_prezime,]