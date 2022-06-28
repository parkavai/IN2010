import java.util.PriorityQueue;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class BalanceHeap{
    public static void main(String[] args) throws IOException{
        // Ved kjoring av programmet, skriv tallene med mellomrom som f.eks slik: 1 2 3 4 5 6 7 8 9 10 
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            PriorityQueue<Integer> heap = new PriorityQueue<>();
            String[] brukerInput = br.readLine().split(" ");
            System.out.println();
            int N = brukerInput.length;
            for (int i = 0; i < N; i++){
                heap.offer(i);
            }
            balansertTre(heap);   
            // Lagd en input.txt hvor outputen fra terminalen kan settes inn filen for å teste om utskriften fungerer i en balansert tre
        }
        catch(IOException e){
            System.out.println("Feil");
        }
    }

    static void balansertTre(PriorityQueue<Integer> A){
        if(A.size() == 0){
            return;
        }
        PriorityQueue<Integer> B = new PriorityQueue<>();
        int halve = (int) A.size()/2;
        while(B.size() < halve){
            B.offer(A.poll());
        }
        System.out.println(A.poll());
        balansertTre(A);
        balansertTre(B);
    }
}