class Korisnik():
    def __init__(self,e_mail,lozinka):
        self._e_mail=e_mail
        self._lozinka=lozinka

@property
def e_mail(self):
    return self._e_mail

@property
def lozinka(self):
    return self._lozinka

def __str__(self):
    return """
    e_mail:{0}
    lozinka {1}
    -------------
    """.format(self._e_mail,self._lozinka)