import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Kattunge{
    public static void main(String[] args) throws IOException{
        ArrayList<Node> listeAvForelder = new ArrayList<>();
        ArrayList<Node> listeAvBarn = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int kattenummer = Integer.parseInt(br.readLine());
        String linje = "";
        while(!(linje.equals("-1"))){
            linje = br.readLine();
            String[] data = linje.split(" ");
            Node parent = new Node(Integer.parseInt(data[0]));
            for(String s: data){
                int tall = Integer.parseInt(s);
                Node barn = new Node(tall);
                if(tall != parent.element){
                    // Hvis vi har en barnenode som også er en foreldernode, så må vi hente den pekeren og sette den til å være parent
                    for(Node n: listeAvBarn){
                        if(n.element == parent.element){
                            parent = n;
                        }
                    }
                    // Hvis vi har en foreldernode som også er en barnenode, så må vi hente pekeren og sette den til å peke på parent
                    for(Node n: listeAvForelder){
                        if(n.element == tall){
                            barn = n;
                        }
                    }
                    barn.forelder = parent;
                    listeAvBarn.add(barn); 
                    listeAvForelder.add(parent);
                }
            }
        }
        for(Node noder: listeAvBarn){
            if(noder.element == kattenummer){
                finnSti(noder);
                return;
            }
        }
    }

    static void finnSti(Node v){
        if(v == null){
            return;
        }
        System.out.print(v.element + " ");
        finnSti(v.forelder);
    }

}