class Racuni():
    def __init__(self,id,datum,osoblje_id,tetovaze_id,ukupno):
        self._id=id
        self._datum=datum
        self._osoblje_id=osoblje_id
        self._tetovaze_id=tetovaze_id
        self._ukupno=ukupno

    @property
    def id(self):
        return self._id

    @property
    def datum(self):
        return self._datum

    @property
    def osoblje_id(self):
        return self._osoblje_id

    @property
    def tetovaze_id(self):
        return self._tetovaze_id

    @property
    def ukupno(self):
        return self._ukupno
        
    def __str__(self):
        return """
        id: {0}
        datum: {1}
        osoblje_id: {2}
        tetovaze_id: {3}
        ukupno: {4}
        ------------
        """.format(self._id,self._datum,self._osoblje_id,self._tetovaze_id,self._ukupno)
    