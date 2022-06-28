"""
Oppgave 1

Oppvarming 2 poeng
• Hva er en algoritme? Svar kort (maks fire setninger).
• Hva er en datastruktur? Svar kort (maks fire setninger).

Hva er en algoritme?
En algoritme realiserer det vi er ute etter å løse i programmering. Skulle det være 
en løsning som finner det største tallet i en liste, så har vi en algoritme som 
gir oss det resultatet.

Hva er en datastruktur?
En datastruktur er en måte organisere dataene på. F.eks så er grafer egnet for 
å strukturere virkeligetsscenarioer som ved bussruter for å vise eventuelle 
destinasjoner som man kan gå fra en gitt stasjon. 

Løsningsforslag
• Algoritmer er idéene bak de programmene vi skriver. De angir hva som må gjøres for å løse et gitt
problem på en presis og entydig måte. Følger du en algoritme for å løse et problem så skal du også få
riktig svar til slutt, og helst på rimelig tid.

• Datastrukturer er måter å organisere data på. Stort sett vil vi organisere dataen etter hva vi oftest
ønsker å gripe tak i, slik at vi kan få mer effektive algoritmer.

Oppgave 3

a.)
------------------------------------------------
Algorithm 1: Er W et subanagram av S?
------------------------------------------------
Input: En streng W og en streng S
Output: Returner true hvis W et subanagram av S, false ellers
------------------------------------------------
1 Procedure IsSubanagramOf1(W, S)
2   r ← copy of W
3       for c in S do
4           if c is in r then
5               remove an occurrence of c from r
6   return r.length = 0
------------------------------------------------

Algoritmen ovenfor skal sjekke om ordet W kan skrives med bokstavene fra S.
• Anta at en streng fungerer akkurat som et array med bokstaver.
• Å kopiere et array gjøres i lineær tid.
• Å sjekke om et element er i et array gjøres i lineær tid.
• Å fjerne et element fra et array gjøres i lineær tid.
• Å finne lengden av et array gjøres i konstant tid.
• Vi lar w angi størrelsen på W og s angi størrelsen på S.

Hva er kjøretidskompleksiteten til algoritmen?
Vi har at kopiering av et array foretas i lineær tid så foreløpig så regnestykket
ser slikt ut ettersom vi foretar en kopi av streng "W" som blir tolket som en array.

O(w)

Deretter har vi en for-løkke hvor vi itererer igjennom elementer i "S" hvor vi får følgende:

O(s)

Videre har vi at vi sjekker om elementet "c" er i et array "r" som gjøres i lineær tid.

O(w)

Deretter har vi at ved fjerning av et element "c" i er "r" så utføres i lineær tid.

O(w)

Tilslutt har vi at lengden av et array gjøres i konstant tid

O(1)

Ved å legge sammen alle disse operasjonene så får vi følgende:

O(w) + (O(s) * (O(w) + O(w))) + O(1))

Nå må vi forenkle uttrykket hvor resultatet blir slikt:

O(w) + (O(s*2w)) + O(1)

Vi kan fjerne konstanten O(1) og O(w) ettersom operasjonen som tar mest tid, er (O(s*2w))

O(s*2w) = O(s*w)

Vi kan fjerne 2 tallet i O(s*2w) ettersom det ikke utgjør en stor forskjell for store O-notasjon

O(s*w) er det riktige svaret. 

b.)

Du skal nå implementere et alternativ til IsSubanagramOf1. Du skal ta utgangspunkt i en frekvenstabell.

Anta at du har en prosedyre FreqTable tilgjengelig, som bygger et map fra bokstaver til antall forekomster i
lineær tid.

Hvis F er en frekvenstabell for strengen "abbcccdddd" vil for eksempel F.get("a") returnere 1 og F.get("d")
returnere 4. Du kan anta at F.get(x) returnerer 0 for alle bokstaver som ikke er med i ordet frekvenstabellen
bygges fra. Du kan oppdatere verdien i frekvenstabellen ved å bruke F.put, som et vanlig map. Både get og
put er i O(1).

Fullfør implementasjonen av IsSubanagramOf2, slik at den har kjøretidskompleksitet O(w + s), der w er
størrelsen av W og s er størrelsen av S.

------------------------------------------------
Algorithm 2: Er W et subanagram av S?
------------------------------------------------
Input: En streng W og en streng S
Output: Returner true hvis W et subanagram av S, false ellers
------------------------------------------------
1 Procedure IsSubanagramOf2(W, S)
2 F ← FreqTable(W)      // Frekvenstabell av F
3 F1 <- FreqTable(S)    // Frekvenstabell av S
4 for c in W:           // Iterer gjennom alle bokstavene i W siden vi skal ha O(w + s), ikke O(s + w)
5   if(F.get(c) > F1.get(c))    // Sjekker om Frekvenstabellen til W, har noen større frekvenser enn i S
6       return False            // Da skal vi returnere False ettersom verdien er ulike
7 return True           // Returnerer True hvis de er like
------------------------------------------------

c.)

Strategi 1    
------------------------------------------------                                                       
1 Procedure SubanagramsOf1(D, S)       
------------------------------------------------                                
2 r ← empty list
3 for i ← 0 to d − 1 do
4     W ← D[i]
5     if IsSubanagramOf2(W, S) then
6        add W to r
7 return r
------------------------------------------------ 
I pseudokoden ovenfor er vi gitt en ordbok D av lengde d, 
som er et array av strenger. Den bruker IsSubanagramOf2 fra 
forrige deloppgave til å finne alle ord i ordboka som er et 
subanagram av S. Å finne subanagrammer med denne teknikken 
kjører i O(d · (w + s)), der d er størrelsen på ordboka, w 
er størrelsen til det største ordet i ordboka, og s er størrelsen til S.

Strategi 2 
------------------------------------------------ 
1 Procedure Build(D)
------------------------------------------------ 
2 M ← empty map
3 for i ← 0 to d − 1 do
4   sortedword ← Sort(D[i])
5   if M.get(sortedword) is empty then
6       M.put(sortedword, empty list)
7   add D[i] to M.get(sortedword)
8 return M
------------------------------------------------ 

------------------------------------------------ 
9 Procedure SubanagramsOf2(M, S)
------------------------------------------------ 
10 r ← empty list
11 for x in sorted substrings of S do
12   append M.get(x) to r
13 return r
------------------------------------------------ 

I pseudokoden ovenfor lager vi et hashmap, der hver nøkkel
k er en streng med bokstaver sortert i alfabetisk rekkefølge,
og verdien er en liste med anagrammer av k som finnes i
ordboka. For å finne alle subanagrammer i ordboken, må vi
slå opp på alle sorterte substrenger av S i hashmapet. Å
finne subanagrammer med denne teknikken kjører i O(2^s),
altså eksponensiell tid med hensyn til størrelsen av S.

Drøft fordeler og ulemper mellom strategi 1 og strategi 2 med tanke på kjøretid.

Strategi 1 bruker O(d · (w + s))

Strategi 2 bruker O(2^s)

Fordeler
Strategi 2 har eksponensiell tid hvor vi vet at kjøretiden kan øke dramatisk 
hvis vi går over et gitt punkt. Så ved lave verdier, kan strategi 2 være god å bruke, 
altså hvor størrelsen til S er relativt lav. 

For strategi 1, så har vi at kjøretiden består av (W, S og D). Hvis ordboken "D"
har en lav størrelse, så er det ikke mange ord som må sammenlignes med "W" og "S"
Dermed kan kjøretiden være rask for dette tilfellet skulle vi ha en slik scenario for 
denne algoritmen. Årsaken er at hvis det er færre ord i ordboken, så er det færre ord å sammenligne 
for "W" og "S" i motsetning til hvis ordboken var ganske stor. Da kan kjøretiden ta 
lang tid. 

Ulemper 
For strategi 2, så er det ikke lurt å benytte store verdier ettersom kjøretiden 
er eksponensiell. Ved tifeller hvr størrelsen til S er stor, så vil kjøretiden være 
lang ved strategi 2. Da er det ikke egnet å benytte denne algoritmen hvis man 
fokuserer kjøretiden. 

For strategi 1, så nevnte jeg tidligere at hvis "D" altså ordboken har en stor størrelse, 
så kan kjøretiden være lang ettersom det er mange ord fra ordboken som sammenlignes med "W" 
og "S". Derfor kan kjøretiden være lang for denne algoritmen. 

d.)
Nå som nettsiden vår har funksjonalitet for å finne subanagrammer av en streng S, gjenstår det bare å presentere
resultatene for brukeren. Anta at subanagrammene som blir returnert av SubanagramsOf2 er gitt som et
array, sortert alfabetisk. Vi ønsker at subanagrammene skal vises sortert etter lengde, og at ord av samme
lengde sorteres alfabetisk, slik som i følgende eksempel:

Input                   Output
"algorithm"             "algorithm"
"alright"               "logarithm"
"git"                   "alright"
"logarithm"             "right"
"math"                  "math"
"right"                 "git"

Fyll ut pseudokode nedfor med så lav kjøretidskompleksitet som mulig.
Algorithm 3: Sortering av subanagrammer
Input: Et array A av størrelse n som inneholder strenger
Output: Et array med de samme n strengene sortert etter lengde der ord av samme lengde er sortert alfabetisk
------------------------------------------------ 
Procedure SortSubanagrams(A)
------------------------------------------------ 
B <- [] // Hashmap  
for i <- 0 to n - 1 do
    k <- A[i].length
    if B[k] <- None
        B[k] <- []
    B[k].append(A[i])
j <- 0 
for k <- 0 to n - 1 do 
    for x in B[k] do
        A[k] = x
        k <- k + 1
Return A
------------------------------------------------ 

Benytter av bucket-sort siden vi har en lenge "n" hvor vi hasher diverse strenger 
til den gitte lengden hvor strengene er sorterte. Bucket-sort gir O(n + N) i 
verste tid men er godt egnet for sorteringen med tanke på kollisjoner og konsistens. 
Kjøretiden vi får fra denne er følgende: O(N log(n) + N) hvor N angir ulike nøkler. 

HTML

a.)

Du innser at det første du må gjøre er å finne alle filene som inneholder feil. 
Etter litt Unix-magi sitter du igjen med filer der all tekst bortsett fra <div> og </div> 
er fjernet. Alt går på skinner frem til du må løse en liten nøtt:
Hvordan sjekker man at det for hver tag som åpnes med <div> også lukkes med </div>, og at
ingen tag lukkes før den er åpnet?
Du må skrive en prosedyre GoodDivs som sjekker dette, med andre ord, at <div>-tagene er velformaterte.
Den tar et array A som argument, der hvert element enten er strengen "<div>" eller strengen "</div>".

------------------------------------------------
Algorithm 6: Avgjøre om <div>-tagene er velformaterte
------------------------------------------------
Input: Et array med "<div>" og "</div>" av lengde n
Output: Returner true hvis tag-ene er velformaterte, false ellers
------------------------------------------------
1 Procedure GoodDivs(A)
2   antallStart = 0
3   antallSlutt = 0 
4   i <- 0
5   for tags in A:
6       if (tags == "<div>")
7           antallStart += 1
8       elif(tags == "</div")
9           antallSlutt += 1
10  if(antallStart != antallSlutt or antallSlutt != antallStart)
11      return False
12  return True

b.)

GoodDivs fungerer som den skal og finner mange filer som inneholder feilformatert HTML. Dessverre oppdager
den ikke alle filene det er rapportert feil på. Du observerer at de inneholder samme feil, men med andre type tager! Altså er det ikke bare <div>-tagene som fører til problemer, men også andre tag-er som <head>, <body>,
<p> og flere andre. Du finner ut at prosedyren GoodDivs må generaliseres til en prosedyre GoodTags.
Hvordan sjekker man at det for hver tag som åpnes også lukkes med en tag av samme type, og at
ingen tag lukkes før den er åpnet?

Du har allerede en enkel prosedyre isOpen, som tar en streng og returnerer true hvis det er en åpne-tag og
false hvis det er en lukke-tag. Altså vil isOpen("<tag>") returnere true og isOpen("</tag>") returnere
false. I tillegg har du en prosedyre som gir deg hvilken type en tag har; for eksempel vil TagType("<div>")
gi "div", og TagType("</p>") gir "p".
------------------------------------------------
Algorithm 7: Avgjøre om tag-ene er velformaterte
------------------------------------------------
Input: Et array A med tag-er av lengde n
Output: Returner true hvis tag-ene er velformaterte, false ellers
------------------------------------------------
1 Procedure GoodTags(A)
for tags in A:
    if()
------------------------------------------------
Hint: Her kan et lurt valg av datastruktur være til stor hjelp.
"""

    