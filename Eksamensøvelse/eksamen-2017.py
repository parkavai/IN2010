"""
Oppgave 2

a.)
Gitt følgende node-klasse:

class BinNode {
int element;
BinNode venstre;
BinNode hoyre;
}
    
Skriv en metode
    boolean sjekkStruktur(BinNode r, BinNode s) { … }
som sjekker om de to binær-trærne med røtter r og s er strukturelt like, det vil si at de har samme node-struktur
når vi ser bort fra verdiene (elementene) i nodene. Lag eventuelt hjelpemetoder hvis det er hensiktsmessig.

Løsningsforslag:
    boolean sjekkStruktur(BinNode r, BinNode s) {
        if (r == null && s == null) {
            return true;
        }
        if (r != null && s != null) {
            return (sjekkStruktur(r.venstre, s.venstre) &&
            sjekkStruktur(r.hoyre, s.hoyre);
        }
        return false;
        }
    }
b.)

Gitt følgende node-klasse (samme som i oppgave 2a):

class BinNode {
int element;
BinNode venstre;
BinNode hoyre;
}

En type balanserte søketrær er AVL-trær. Tilleggskravet er da at for hver node skal høyden til de to subtrærne
ha en forskjell på max 1. Et tomt tre er definert til å ha høyde -1. Skriv en metode

    boolean sjekkAVL(BinNode n) { … }

som sjekker om dette AVL-kravet er oppfylt for treet med rot-node n. Lag evt hjelpemetoder hvis det er
hensiktsmessig.

Procedure sjekkAVL(n):
    hoydeForskjell = hentHoydeVenstre(n.venstre) - hentHoydeHoyre(n.hoyre)
    if(hoydeForskjell < -1 or hoydeForskjell > 1){
        return False
    }
    return True

Procedure hentHoydeVenstre(x):
    if(x == null):
        return -1
    return 1 + hentHoyde(x.venstre)

Procedure hentHoydeHoyre(x):
    if(x == null):
        return -1
    return 1 + hentHoyde(x.hoyre)

Løsningsforslag

boolean sjekkAVL(BinNode n) {
// Bruker -2 som feilverdi i hjelpemetoden.
return (sjekkHoyde(n) != -2);
}
int sjekkHoyde(BinNode n) {
    if (n == null) 
        return -1;

    int v = sjekkHoyde(n.venstre);
    if (v == -2) 
        return v;

    int h = sjekkHoyde(n.hoyre);
    if (h == -2) 
        return h;

    if (Math.abs(v-h) > 1) 
        return -2;
    return (Math.max(v,h) + 1);
}

"""