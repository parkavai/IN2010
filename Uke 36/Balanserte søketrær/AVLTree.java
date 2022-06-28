class AVLTree {

    class Node {
        int x;
        int height;
        Node left;
        Node right;

        Node(int x) {
            this.x = x;
            this.height = 1;
        }
    }

    Node root;

    void insert(int x){
        root = insert(root,x);
    }

    Node insert(Node v, int x){
        if(v == null){
            return new Node(x);
        }
        else if(x < v.x){
            v.left = insert(v.left,x);
        }
        else if(x > v.x){
            v.right = insert(v.right,x);
        }
        v.height = 1 + max(height(v.left), height(v.right));
        return balance(v);
    }

    void delete(int x){
        root = delete(root, x);
    }

    Node delete(Node v, int x){
        if(v == null){
            return null;
        }
        else if(x < v.x){
            v.left = delete(v.left,x);
        }
        else if(x > v.x){
            v.right = delete(v.right,x);
        }
        else if(v.right == null){
            v = v.left;
        }
        else if(v.left == null){
            v = v.right;
        }
        else {
            Node u = findMin(v.right);
            v.x = u.x;
            v.right = delete(v.right,u.x);
        }
        return v;
    }

    // Henter løvnode med minst verdi, som befinner seg lengst til venstre
    Node findMin(Node v){
        if(v.left == null){
            return v;
        }
        return findMin(v.left);
    }

    boolean contains(int x){
        return contains(root,x);
    }

    boolean contains(Node v, int x){
        if(v == null){
            return false;
        }
        else if(x < v.x){
            return contains(v.left,x);
        }
        else if(x > v.x){
            return contains(v.right,x);
        }
        return true;
    }

    void inorder(){
        inorder(root);
    }

    void inorder(Node v){
        if(v == null){
            return;
        }
        inorder(v.left);
        System.out.println(v.x);
        inorder(v.right);
    }

/*
    Før høyrerotasjon(er venstretung,dermed en høyrerotasjon):                     Etter høyrerotasjon:                        
                    z                                                                       y
                y      T3                                                           x               z
            x       T2                                                          T0     T1       T2     T3
        T0     T1
*/
                                        
    Node rightRotate(Node z){
        Node y = z.left;
        Node T2 = y.right;

        // Utfører rotasjonen, visuelt bilde over som viser hvordan dette foregår
        z.left = T2;
        y.right = z;

        // Oppdatere høydene til både z og y siden vi har utført rotasjonen
        z.height = 1 + max(height(z.left), height(z.right));
        y.height = 1 + max(height(y.left), height(y.right));

        // Henter den nye roten
        return y;

    }

/*
            Før venstrerotasjon:                                                Etter venstrerotasjon:                        
                    z                                                                       y
                T0      y                                                           z               x
                    T1      x                                                  T0     T1       T2      T3
                        T2      T3
                                        
*/
    Node leftRotate(Node z) {
        Node y = z.right;
        Node T1 = y.left;
 
        // Utfører rotasjon, visuelt bilde over hvordan dette utføres, er vist over
        y.left = z;
        z.right = T1;
 
        //  Oppdaterer høyden til både z og y da rotasjonen endrer høyden til begge noder
        z.height = max(height(z.left), height(z.right)) + 1;
        y.height = max(height(y.left), height(y.right)) + 1;
 
        // Returnerer den nye roten siden z ikke lenger er roten. 
        return y;
    }

    // Hjelpefunksjon for å kunne utføre algoritmene i avl-trær, dette er da høyden for en gitt node
    int height(Node N) {
        if (N == null)
            return 0;

        return N.height;
    }
 
    // Hjelpefunksjon for å kunne utføre algoritmene i avl-trær, dette er da max
    int max(int a, int b) {
        return (a > b) ? a : b;
    }

    int balancefactor(Node v){
        if(v == null) {
            return 0;
        }
        // Returnerer en høydeforskjellen mellom venstre og høyresubtre for node "v"
        return height(v.left) - height(v.right);
    }

    Node balance(Node v){
        // Hvis betingelsen oppfylles, så betyr det at treet er høyretung, dette kan sees hvis du forestiller det
        if (balancefactor(v) < -1){
            // Må foreta en høyrerotasjon i høyresubtre, 
            if(balancefactor(v.right) > 0){
                v.right = rightRotate(v.right);
            }
            return leftRotate(v);
        }
        // Hvis betingelsen oppfylles, så betyr det at treet er venstretung, dette kan sees hvis du forestiller det
        if (balancefactor(v) > 1){
            // Må sjekke hvis 
            if(balancefactor(v.left) < 0){
                v.left = leftRotate(v.left);
            }
            return rightRotate(v);
        }
        return v;
    }

    public static void main(String[] args) {
        AVLTree t = new AVLTree();
        t.insert(10);
        t.insert(20);
        t.insert(30);
        t.insert(40);
        t.insert(50);
        t.insert(25);
        t.inorder();
    }
}