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
        if len(self.kassaKo) > 0:
            if self.kassaKo[0].varDetAllt() > 0:
                return self.kassaKo[0].tick()
            else:
                return self.nyKund()
        else:
            return -1

    def printRes(self, numVaror):
        if numVaror >= 0:
            print("kassa ", self.num, " har ", len(self.kassaKo) ,"kunder i kön och första kunden har ", numVaror, " varor")
        else:
            print("kassa ", self.num, " är tom")
        
    def tick(self):
        if not self.open:
            return
        
        if rand.random() < 0.25:
            self.kassaKo.append(kund.Kund())

        numVaror = self.hanteraKund()
        self.printRes(numVaror)
        
    def whoami(self):
        return self.num
