"""
Fasit: https://www.uio.no/studier/emner/matnat/ifi/IN2010/h21/eksamens-ressurser/in2010-h2019-sensorveiledning.pdf

Oppgave 1 

a.) 
Anta at G er en sammenhengende graf med 12 noder og 20 kanter og at S er et spenntre for G.
Hvor mange kanter har S?

Det er 11 kanter ettersom vi skal finne et spenntre for G som vil si at vi skal finne den 
korteste stien hvor vi traverserer gjennom alle kanter som fører til en ny node som ikke 
er blitt besøkt enda. Noder som er blitt besøkt vil vi unngå å måtte traversere igjennom 
så derfor vil antall kanter i et spenntre synke. Svaret er 11 ettersom det er 12 noder og 
for å finne antall kanter i et spenntre så utføres følgende regneoperasjon: N-1 hvor N 
tilsvarer antall noder.  

b.)
Sjekk fasit pga av at bildet for grafen ikke er oppgitt.

c.)
Kryss av for den, eller de algoritmene, som gitt en sammenhengende vektet graf, finner
et minimalt spenntre for grafen.

Bredde-først-søk (BFS)
Kruskal                     X
Dybde-først-søk (DFS)
Prim                        X
Borůvka                     X

De som er markert med "X" er de rette svarene som er blitt krysset. Årsaken til at det 
er disse algoritmene er, fordi vi skal plukke ut de algoritmene som finner et minimalt 
spenntre for grafen. Dvs, trær hvor vi finner korteste vei gjennom å følge vekten til 
kantene i grafen. De som er krysset er algoritmer som er ansvarlige for å finne kanter 
med vekter. BFS og DFS gir oss et spenntre, men ikke et minimalt spenntre. 

i.)
Gitt en hashtabell av lengde 5 som kan lagre heltall.
Vi bruker lukket hashing med lineær prøving og hashfunksjonen h(k) = k mod 5 .
Vi legger følgende elementer inn i tabellen i denne rekkefølgen:

17, 98, 59, 32, 40

På hvilken indeks havner siste element (40)?

17: indeks 2 
98: indeks 3
59: indeks 4(siste indeks)
32: indeks 0(vi har ikke indeks 7 ikke ettersom lengden er 5 så den kommer til neste ledige plass)
40: indeks 1 

Indeks 1 er det riktige svaret

Oppgave 2

f.)

En spilldesigner har laget et forslag til en verden og representert den som en rettet graf . Du blir
bedt om å sjekke om verdenen representert ved har følgende egenskaper:

verdenen har nøyaktig ett skattkammer
verdenen har nøyaktig tre startrom.

Skriv en algoritme som sjekker om en foreslått verden har de to egenskapene over.
For enkelhetsskyld kan du anta at du får inn grafen som input.
Du kan også anta at du for hver node får en liste over utgående- og innkommende kanter for noden.
Her kan du, om ønskelig, gjenbruke resultater fra de tidligere deloppgavene (selv de du ikke har besvart).
Du kan bruke naturlig språk og/eller pseudokode for å beskrive algoritmen din.
I tillegg er det mulig å gjenbruke algoritmer vi har sett på i IN2010. Hvis du for eksempel ønsker å traversere
grafen med dybde-først søk, trenger du ikke å forklare hvordan dybde-først søk fungerer. Hvis du ønsker å
benytte en modifisert versjon av en algoritme fra kurset, må modifikasjonene komme tydelig frem.
I IN2010 har vi lagt vekt på effektive algoritmer. I denne oppgaven vil derfor en rask algoritme gi større uttelling
enn en mindre rask algoritme.
I neste oppgave blir du bedt om å analysere kjøretiden til algoritmen din.

Procedure spillverden(G):
    S = new Empty Stack
    Skatt = []
    for each vertex v in G do 
        inCount(v) = degree in(v)
        if inCount(v) = 0 then
            S.push(v)
    if(len(S) != 3) then
        return False
    i = 1
    while S not empty do
        v = S.pop()
        if(outCount(v) = 0)
            Skatt.append(v)
        output[i] = x
        i = i + 1
        for each edge(v,w) in G do
            inCount(w) = inCount(w) - 1
            if inCount(w) =  0 then 
                S.push(w)
    if(len(Skatt) > 1) then
        return False
    return True

"""