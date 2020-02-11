class Recenzije():
    def __init__(self, ocjena, tetovaze_id, korisnik_id):
        self._ocjena=ocjena
        self._tetovaze_id=tetovaze_id
        self._korisnik_id=korisnik_id

@property
def ocjena(self):
    return self._ocjena

@property
def tetovaze_id(self):
    return self._tetovaze_id

@property
def korisnik_id(self):
    return self._korisnik_id

def __str__(self):
    return """
    ocjena: {0}
    tetovaze_id:{1}
    korisnik_id {2}
    -------------
    """.format(self._ocjena,self._tetovaze_id,self._korisnik_id)