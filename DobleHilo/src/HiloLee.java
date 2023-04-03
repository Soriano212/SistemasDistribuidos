import java.util.ArrayList;

public class HiloLee extends Thread {
    private ArrayList<Integer> lista;

    public HiloLee(String string, ArrayList<Integer> lista) {
        super(string);
        this.lista = lista;
    }

    public void run() {
        while (lista.size() <= 25) {
            synchronized (lista) {

                try {
                    lista.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

            }

            System.out.println("HiloLee: ");
            for (int elemento : lista) {
                System.out.print(elemento + " ");
            }
            System.out.println("|  Cantidad: " + lista.size());
        }

    }
}
