"""
Oppgave 3

I et binært søketre har vi noder med heltallsverdier. Vi definerer en nodes plassering i treet med en
tekststreng slik: RLLRLR 761
Dette betyr at det i treet finnes en node med verdi 761, og for å finne noden må vi fra rota først
følge kanten mot høyre (R), så mot venstre (L), så venstre, høyre, venstre, høyre.

Nytt:
Gitt følgende nodeklasse:
    class Node {
    Node l, r; // left, right
    int v; // value
    IN2010/INF2220 eksamen 2018 med engelsk
    4/13
}
Skriv en Java/Python-metode "writePathToNode" som gitt en verdi leter i treet og skriver ut stien og verdien
hvis det finnes en node med denne verdien i treet. Det er ikke tillatt å endre nodeklassen, men du kan
lage hjelpemetoder hvis du mener det er hensiktsmessig. Eksempel på utskrift:
"""

# Svar: 
def writeToPath(node, verdi, veien):
    if(node == None):
        print("Verdien " + verdi + " finnes ikke i treet.")
        return 
    elif(node.v == verdi):
        print(veien + str(verdi))
        return 
    elif(verdi < node.v):
        veien += "L"
        writeToPath(node.left, verdi, veien)
    elif(verdi > node.v):
        veien += "R"
        writeToPath(node.right, verdi, veien)
    

"""
Oppgave 4

I et binært søketre har vi noder med heltallsverdier. Vi definerer en nodes plassering i treet med en
tekststreng slik: RLLRLR 761

Dette betyr at det i treet finnes en node med verdi 761, og for å finne noden må vi fra rota først
følge kanten mot høyre (R), så mot venstre (L), så venstre, høyre, venstre, høyre.
Gitt følgende nodeklasse:
    class Node {
    Node l, r; // left, right
    int v; // value
}

Nytt:
Skriv en Java/Python-metode removeLessThan (Node n, int value) slik at hvis Node root er et binært
søketre, vil tilordningen

                    root = removeLessThan(root, value);

fjerne alle noder med verdier mindre enn value fra treet. Du kan lage hjelpemetoder hvis du mener det
er hensiktsmessig.
"""

# Svar: 
def removeLessThan(node,value):
    if(node == None):
        return 
    # Hvis verdien er mindre eller lik roten, så skal vi kun fokusere på noder i venstre subtre 
    elif(value <= node.v):
        node.left = removeLessThan(node.l,value)
        return node
    # Da skal vi fjerne de nodene som har verdi mindre enn "value"
    elif(value > node.v):
        return removeLessThan(node.r,value)
    
    
"""
Oppgave 5

Vi skal legge disse tallverdiene inn i en hashtabell med lengde 11:
{42, 78, 57, 18, 12, 74, 99, 20, 33, 61, 19, 91}

I denne oppgaven skal du bruke hashfunksjonen
    h ( k ) = k mod 11

a) Angi om du vil du vil benytte åpen eller lukket hashing og evt. hvilke tillegssfunksjoner du bruker
utenom h. Begrunn svaret.

Svar: 
Jeg ville ha benyttet "Separate chaining"/åpen hashing. Grunnen ligger i at det vil oppstå et problem 
ved "Linear probing"/lukket hashing. Ved bruk av lukket hashing, så vil vi ha en hashtabell med indeks 
fra 0 til 10. Ved å lage denne tabellen, så kan vi se problemet ved denne tabellen.

{42: indeks 9 
78: indeks 1, 
57: indeks 2 
12: indeks 3
74: indeks 8
99: indeks 0
20: indeks 10
33: indeks 4
61: indeks 6
19: indeks 5}

91 vil ikke få plass inn i denne hashtabellen og derfor er ikke "Linear probing" ideelt i dette tilfellet

b) Deretter viser du hvordan hashtabellen blir.
Svaret skal være 11 linjer; én indeks pr. linje på denne måten:
indeks: verdi [, verdi]
indeks: verdi [, verdi]
indeks: verdi [, verdi]
Verdiene skrives med komma i mellom hvis flere verdier på én indeks. La verdien som kommer først
på indeksen stå lengst til venstre. La det være tomt etter kolonet hvis det ikke er noen verdi på
indeksen.

Svar:
{
0: 99, 33
1: 78, 12
2: 57
3: 91
4: 
5: 
6: 61
7: 18
8: 74, 19
9: 42,10
10:    
}
"""

"""
Skriv kode for metoden put som setter et element e (av type Element) inn i tabellen hashTable:
    Object [ ] hashTable = new Object[n];

Nøkkelen til e finnes i e.k, som er en int variabel.
"put" skal bruke lukket hashing med lineær prøving. 

    Hashfunksjonen er h(x) = x mod n. 

Metoden skal returnere true/false avhengig av om elementet ble satt inn eller ikke.

Skriv ditt svar
"""

#Svar
def put(element, hashtable):
    n = len(hashtable)-1
    indeks = element.k % n
    if(indeks > n):
        return False 
    i = 0
    while(i in range(n)):
        if(hashtable[indeks] == None):
            hashtable[indeks] = element
            return True 
        elif(hashtable[indeks].k == element.k):
            hashtable[indeks] = element
            return True 
        i += 1
        indeks = (indeks+1) % n
    return False

"""
Oppgave 7

Gitt følgende array (index 0 er tom). Representerer dette arrayet en heap? Begrunn svaret.
[ , 9, 5, 7, 8, 25, 13, 9, 6]

Svar:
                    9
            5               7
        8       25      13      9
    6      

Vi ser at det ikke funker ettersom rotnoden "9" ikke er det minste/største tallet. I heaps, så er det et krav 
at, hvis heapen er en "min-heap" så skal det minste tallet være rotnoden og som vi går nedover mot treet så 
skal barna være mindre enn foreldrene og motsatt ved "max-heap". Men her vet vi ikke om rotnode "9" er det 
minste eller største og derfor er ikke arrayen en heap. 
"""

"""
Oppgave 8

Basert på følgende frekvens av tegn, tegn det resulterende huffmantreet og gi tegnenes huffmankoder.
A(106), B(200), C(500), D(701), E(305)

Når vi skal lage et huffmantre, så må vi se på frekvensen for en gitt symbol og ta de minste som løvnoder.
A er da den minste og vi bygger oss oppover fra denne noden. Rekkefølgen vil være A,B,E,C,D hvor bitstrengen 
vil være følgende for hver symbol:

A = 0000
B = 0001
E = 001
C = 01
D = 1

"""