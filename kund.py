import random as rand

class Kund:
    def __init__(self):
        self.numVaror = rand.randrange(1, 10)

    def tick(self):
        if self.numVaror > 0:
            self.numVaror -= 1
        return self.numVaror
    
    def varDetAllt(self):
        return self.numVaror
