import math

class Node:
    def __init__(self, data):
        self.data = data
        self.besokt = False
        self.inDeg = 0
        self.naboer = []

    def __str__(self):
        penStr = str(self.data) + ": ["
        if (len(self.naboer) != 0):
            for kant in self.naboer:
                penStr += str(kant.data) + ", "
            penStr = penStr[:len(penStr) - 2]  #fjerner trailing komma
        return penStr + "]"

class Kant: 
    def __init__(self, u, v, vekt):
        self.u = u
        self.v = v
        self.vekt = vekt

class Graf:
    def __init__(self, rettet):
        self.graf = {}
        self.kanter = {}
        self.rettet = rettet

    def leggTilKant(self, u, v, vekt):
        kant = Kant(u,v, vekt)
        self.kanter[vekt] = kant
    
    def hentKant(self,u,v,vekt):
        if (vekt not in self.kanter):
            self.kanter[vekt] = Kant(u,v)
        return self.kanter[vekt]

    def hentNode(self, data):
        if (data not in self.graf):
            self.graf[data] = Node(data)
        return self.graf[data]

    def __str__(self):
        penStr = ""
        for v in self.graf:
            penStr += str(self.graf[v]) + "\n"
        return penStr

class Spenntre:
    def __init__(self, G):
        self.G = G
        self.vekt = 0
    



    
def main():
    foilGraf = Graf(False)
    foilGraf.leggTilKant("A", "B", 13)
    foilGraf.leggTilKant("A", "C", 6)
    foilGraf.leggTilKant("B", "C", 7)
    foilGraf.leggTilKant("B", "D", 1)
    foilGraf.leggTilKant("C", "D", 14)
    foilGraf.leggTilKant("C", "E", 8)
    foilGraf.leggTilKant("D", "E", 9)
    foilGraf.leggTilKant("D", "F", 3)
    foilGraf.leggTilKant("E", "F", 2)
    foilGraf.leggTilKant("E", "J", 18)
    foilGraf.leggTilKant("J", "L", 4)
    foilGraf.leggTilKant("H", "J", 17)
    foilGraf.leggTilKant("H", "G", 15)
    foilGraf.leggTilKant("H", "C", 20)
    foilGraf.leggTilKant("G", "I", 5)
    foilGraf.leggTilKant("J", "K", 16)
    foilGraf.leggTilKant("K", "I", 11)
    foilGraf.leggTilKant("L", "K", 12)
    print(foilGraf)

main()