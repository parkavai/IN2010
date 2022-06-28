import java.util.ArrayList;
import java.lang.Math;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Teque{

    private ArrayList<Integer> A;

    public Teque(ArrayList<Integer> liste){
        this.A = liste;
    }

    public void push_back(int x){
        A.add(x);
    }

    public void push_middle(int x){
        int k = A.size();
        if(k > 1){
            int posisjon = (int) Math.floor((k+1)/2);
            ArrayList<Integer> B = new ArrayList<>();
            int teller = 0;
            for (int element: A){
                if(teller == posisjon){
                    B.add(x);
                }
                B.add(element);
                teller += 1;
            }
            A = B;
        }
        else {
            A.add(x);
        }
    }
    
    public void push_front(int x){
        ArrayList<Integer> B = new ArrayList<>();
        B.add(x);
        for (int element: A){
            B.add(element);
        }
        A = B;
    }

    public int get(int i){
        return A.get(i);
    }


    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> liste = new ArrayList<>();
        Teque teque = new Teque(liste);
        for (int i = 0; i < N; i++){
            String[] line = br.readLine().split(" ");
            String prosedyre = line[0];
            int x = Integer.parseInt(line[1]);
            if(prosedyre.equals("push_front")){
                teque.push_front(x);
            }
            else if(prosedyre.equals("push_middle")){
                teque.push_middle(x);
            }
            else if(prosedyre.equals("push_back")){
                teque.push_back(x);
            }
            else if(prosedyre.equals("get")){
                System.out.println(teque.get(x));
            }
            else{
                System.out.println("Ugyldig prosedyre" + prosedyre);
                break;
            }
        }
    }
}