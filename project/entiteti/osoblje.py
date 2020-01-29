class Osoblje():
    def __init__(self,id,ime,prezime,datumpocetkarada,brojtetovazaizradenih):
        self._id=id
        self._ime=ime
        self._prezime=prezime
        self._datumpocetkarada=datumpocetkarada
        self._brojtetovazaizradenih=brojtetovazaizradenih

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

def __str__(self):
    return """
    id: {0}
    ime: {1}
    prezime: {2}
    datumpocetkarada: {3}
    brojtetovazaizradenih: {4}
    -------------
    """.format(self._id,self._ime,self._prezime,self._datumpocetkarada,self._brojtetovazaizradenih)