import java.util.ArrayList;

public class Binaersoek {

    public static void main(String[] args) {
        ArrayList<Integer> talliste = new ArrayList<>();
        talliste.add(1);
        talliste.add(2);
        talliste.add(3);
        talliste.add(4);
        talliste.add(5);
        talliste.add(6);
        talliste.add(7);
        talliste.add(8);
        System.out.print(binaersoek(talliste,7));
    }

    static Boolean binaersoek(ArrayList<Integer> liste, int x){
        int low = liste.get(0);
        int high = liste.get(liste.size() -1);
        while (low < high) {
            int index = (int) (low+high)/2;
            System.out.println(index);
            if(liste.get(index) == x){
                return true;
            }
            else if(liste.get(index) < x){
                low = index + 1;
            }
            else if(liste.get(index) > x){
                high = index - 1;
            }
        }
        return false;
    }
    
}
