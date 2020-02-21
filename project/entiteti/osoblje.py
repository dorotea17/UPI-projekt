class Osoblje():
    def __init__(self,id,ime_prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka):
        self._id=id
        self._ime_prezime=ime_prezime
        self._datumpocetkarada=datumpocetkarada
        self._brojtetovazaizradenih=brojtetovazaizradenih
        self._e_mail=e_mail
        self._lozinka=lozinka

    @property
    def id(self):
        return self._id

    @property
    def ime_prezime(self):
        return self._ime_prezime

    @property
    def datumpocetkarada(self):
        return self._datumpocetkarada

    @property
    def brojtetovazaizradenih(self):
        return self._brojtetovazaizradenih

    @property
    def e_mail(self):
        return self._e_mail

    @property
    def lozinka(self):
        return self._lozinka

    def __str__(self):
        return """
        id: {0}
        ime_prezime: {1}
        datumpocetkarada: {2}
        brojtetovazaizradenih: {3}
        e_mail: {4}
        lozinka: {5}
        -------------
        """.format(self._id,self._ime_prezime,self._datumpocetkarada,self._brojtetovazaizradenih,self._e_mail,self._lozinka)