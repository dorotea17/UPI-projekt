class Korisnik():
    def __init__(self, id, e_mail,lozinka):
        self._id=id
        self._e_mail=e_mail
        self._lozinka=lozinka

@property
def id(self):
    return self._id

@property
def e_mail(self):
    return self._e_mail

@property
def lozinka(self):
    return self._lozinka

def __str__(self):
    return """
    id: {0}
    e_mail:{1}
    lozinka {2}
    -------------
    """.format(self._id,self._e_mail,self._lozinka)