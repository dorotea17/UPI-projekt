class Osoblje():
    def __init__(self,id,ime,prezime,datumpocetkarada,brojtetovazaizradenih,e_mail,lozinka):
        self._id=id
        self._ime=ime
        self._prezime=prezime
        self._datumpocetkarada=datumpocetkarada
        self._brojtetovazaizradenih=brojtetovazaizradenih
        self._e_mail=e_mail
        self._lozinka=lozinka

@property
def id(self):
    return self._id

@property
def ime(self):
    return self._ime

@property
def prezime(self):
    return self._prezime

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
    ime: {1}
    prezime: {2}
    datumpocetkarada: {3}
    brojtetovazaizradenih: {4}
    e_mail: {5}
    lozinka: {6}
    -------------
    """.format(self._id,self._ime,self._prezime,self._datumpocetkarada,self._brojtetovazaizradenih,self._e_mail,self._lozinka)