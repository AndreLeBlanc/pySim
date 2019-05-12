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

class Gamling(Kund):
    def tick(self):
        if rand.random() < 0.5:
            return super().tick()
        else:
            return super().varDetAllt()
