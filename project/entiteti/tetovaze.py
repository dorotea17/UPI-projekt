class Tetovaze():
    def __init__(self,id,link,naziv,velicina,vrijeme,cijena):
        self._id=id
        self._link=link
        self._naziv=naziv
        self._velicina=velicina
        self._vrijeme=vrijeme
        self._cijena=cijena

@property
def id(self):
    return self._id

@property
def link(self):
    return self._link

@property
def naziv(self):
    return self._naziv

@property
def velicina(self):
    return self._velicina

@property
def vrijeme(self):
    return self._vrijeme

@property
def cijena(self):
    return self._cijena

def __str__(self):
    return """
    id: {0}
    link: {1}
    naziv: {2}
    velicina: {3}
    vrijeme: {4}
    cijena: {5}
    ---------------
    """.format(self._id,self._link,self._naziv,self._velicina,self._vrijeme,self._cijena)