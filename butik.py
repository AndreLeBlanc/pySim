import kund
import kassa

class Butik:
    def verifiera(self, numKassa):
        return (0 <= numKassa) and (numKassa < 32)
    
    def __init__(self, numKassa):
        if self.verifiera(numKassa):
            print("öppnar butik")
            self.kassor = []
            for i in range(1, numKassa+1):
                self.kassor.append(kassa.Kassa(i))

    def isKassa(self, num):
        return (0 < num) and (num < len(self.kassor))

    def stangKassa(self, num):
        if self.isKassa(num):
            self.kassor[num-1].close()

    def oppnaKassa(self, num):
        if self.isKassa(num):
            self.kassor[num-1].openKassa()

    def vilkaKassor(self):
        for i in self.kassor:
            print(i.whoami())

    def kassaMangd(self):
        print(len(self.kassor))

    def tick(self):
        for i in self.kassor:
            i.tick()
