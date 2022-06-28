class Node:
    def __init__(self, element, posisjon, rad):
        self.element = element
        self.left = None
        self.right = None
        self.posisjon = posisjon
        self.rad = rad
    
    def __str__(self):
        return str(self.element)

def hent(height, streng):
    height = int(height)
    streng = str(streng)
    rot = (2**height) - 1
    tall = 0
    for i in range(len(streng)-1):
        if(streng[i] == "L"):
            tall = (2 * tall) + 1
        else:
            tall = (2 * tall) + 2
    tall = rot - tall 
    return tall

def main():
    fil = input().split()
    print(hent(fil[0],fil[1]))

main()