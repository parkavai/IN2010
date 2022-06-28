import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BalanceArray {
    public static void main(String[] args){
        // Ved kjoring av programmet, skriv tallene med mellomrom som f.eks slik: 1 2 3 4 5 6 7 8 9 10 
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String[] stringArr = br.readLine().split(" ");
            System.out.println();
            int N = stringArr.length;
            int[] sortertListe = new int[N];
            for(int i = 0; i < N; i++){
                sortertListe[i] = i;
            }
            balansertTre(sortertListe, 0, sortertListe.length-1);
            // Lagd en input.txt hvor outputen fra funksjonen, kan settes inn for å teste om utskriften fungerer i en balansert tre
        }
        catch(IOException e){
            System.out.println("Feil");
        }
    }

    static void balansertTre(int[] A, int low, int high){
        // Basissteget hvor vi ikke skal rekursere hvis low > high for da vil høydeforskjellen bli venstretung, dermed ikke "helt" balansert
        if(low > high){
            return;
        }
        // Skriver ut midterste element
        System.out.println(A[hentMidten(low, high)]);
        // Hoyre subtre
        balansertTre(A, hentMidten(low, high) + 1, high);;
        // Venstre subtre
        balansertTre(A, low, hentMidten(low, high) - 1);
    }

    static int hentMidten(int low, int high){
        return (int) (low+high)/2;
    }
}
