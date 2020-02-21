import unittest
import os,sys,sqlite3,datetime

from baza import *
dirname=os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\','/')+'/entiteti/')

from korisnik import Korisnik
from racuni import Racuni
from osoblje import Osoblje
from tetovaze import Tetovaze
class TestStringMethods(unittest.TestCase):

    def test_init_e_mail_error(self):
        with self.assertRaises(ValueError):
            Korisnik("db@","")

    def test_init_lozinka_error(self):
        with self.assertRaises(ValueError):
            Korisnik("","123")

    def test_init_sacuvaj_novi_racun(self):
        lista_unos=["2020-01-01","Ivana Konta","Ptica",500]
        sacuvaj_novi_racun(lista_unos[0],lista_unos[1],lista_unos[2],lista_unos[3])

        p=procitaj_podatke_racuna()
        i=len(p)-1
        lista_rezultat = [p[i][1]._datum,p[i][2]._ime_prezime,p[i][0]._naziv,p[i][1]._ukupno]

        self.assertEqual(lista_rezultat,(lista_unos))
        print("\nsacuvaj_novi_racun")
        print("Unešeni podaci")
        print(lista_unos)
        print("Rezultat")
        print(lista_rezultat)

    def test_init_azuriraj_racun(self):
        lista_unos=["1","2019-12-12","Ivana Konta","Zmaj",3000]
        azuriraj_racun(lista_unos[0],lista_unos[1],lista_unos[2],lista_unos[3],lista_unos[4])

        l=dohvati_racun_po_id("1")
        lista_rezultat=[str(l[1]._id),l[1]._datum,l[2]._ime_prezime,l[0]._naziv,l[1]._ukupno]

        self.assertEqual(lista_rezultat, (lista_unos))
        print("\nazuriraj_racun")
        print("Unešeni podaci")
        print(lista_unos)
        print("Rezultat")
        print(lista_rezultat)

    def test_init_sacuvaj_korisnika(self):
        unos = ["korisnik@pmfst.hr", "korisnik"]
        sacuvaj_korisnika(unos[0], unos[1])

        l = procitaj_podatke_korisnik()
        i = len(l) - 1
        rezultat = [l[i]._e_mail, l[i]._lozinka]

        self.assertEqual(rezultat, (unos))
        print("\nsacuvaj_korisnika")
        print("Unešeni podaci")
        print(unos)
        print("Rezultat")
        print(rezultat)
    
    


unittest.main()