import java.util.ArrayList;

public class HiloLee extends Thread{
    private ArrayList<Integer> lista;

    public HiloLee (String string, ArrayList<Integer> lista){
        super(string);
        this.lista = lista;
    }
    public void run() {
        synchronized (lista) {
            while (lista.size() == 0){
                try {
                    lista.wait();
                    System.out.println("Ingresa");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            for (int elemento : lista) {
                System.out.print(elemento + " ");
            }
            
        }
    }
}
