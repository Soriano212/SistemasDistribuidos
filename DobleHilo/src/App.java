import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws InterruptedException {
        ArrayList<Integer> lista = new ArrayList<Integer>(0);
        HiloAgrega hiloAgrega = new HiloAgrega("HiloAgregar", lista);
        HiloLee hiloLee = new HiloLee("HiloLeer", lista);

        hiloAgrega.start();
        hiloLee.start();
    }
}
