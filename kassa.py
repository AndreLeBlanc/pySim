import kund as kund
import random as rand

class Kassa:
    def __init__(self, num):
        print("kassa ", num, " installerad")
        self.open = False
        self.num = num
        
    def close(self):
        self.open = False
        print("kassa ", self.num, " stängd")
        
    def openKassa(self):
        self.open = True
        print("kassa ", self.num, " öppen")
        self.kassaKo = []

    def nyKund(self):
        self.kassaKo.pop(0)
        if len(self.kassaKo) > 0:
            return self.kassaKo[0].varDetAllt()
        return -1
    
    def hanteraKund(self):
        if 0 < len(self.kassaKo):
            if 0 < self.kassaKo[0].varDetAllt():
                return self.kassaKo[0].tick()
            else:
                return self.nyKund()
        else:
            return -1

    def printRes(self, numVaror):
        if 0 <= numVaror:
            print("kassa ", self.num, " har ", len(self.kassaKo) ,"kunder i kön och första kunden har ", numVaror, " varor")
        else:
            print("kassa ", self.num, " är tom")

    def kanskeLaggTillKund(self):
        if not self.open:
            return
        odds = rand.random()
        print(odds)
        if odds < 0.25:
            self.kassaKo.append(kund.Kund())
        elif odds < 0.3:
            self.kassaKo.append(kund.Gamling())
        
    def tick(self):
        print("ej snabbkassetick")
        self.kanskeLaggTillKund()
        numVaror = self.hanteraKund()
        self.printRes(numVaror)
        
    def whoami(self):
        return self.num

    def __delete__(self):
        print("died")

class SnabbKassa(Kassa):
    def __init__(self, num):
        self.unBlocked = True
        super().__init__(num)

    def tick(self):
        print("snabbkasse tick")
        if self.unBlocked:
            super().kanskeLaggTillKund()
            numVaror = self.hanteraKund()
            if numVaror == -2:
                print("fel Kassa")
            super().printRes(numVaror)
        else:
            felPlats = self.kassaKo[0]
            self.kassaKo.pop()
            self.unBlocked = True
            return felPlats
        
    def nyKund(self):
        self.kassaKo.pop(0)
        if 0 < len(self.kassaKo):
            if 5 < self.kassaKo[0].varDetAllt():
                self.unBlocked = False
                return -2
            return self.kassaKo[0].varDetAllt()
        return -1

    def hanteraKund(self):
        if 0 < len(self.kassaKo):
            if 5 < self.kassaKo[0].varDetAllt():
                self.unBlocked = False
                return -2
            elif 0 < self.kassaKo[0].varDetAllt():
                return self.kassaKo[0].tick()
            else:
                return self.nyKund()
        else:
            return -1
    
