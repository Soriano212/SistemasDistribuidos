import java.util.ArrayList;

public class HiloAgrega extends Thread{
    private ArrayList<Integer> lista;

    public HiloAgrega (String string, ArrayList<Integer> lista){
        super(string);
        this.lista = lista;
    }
    public void run() {

            for (int i=0; i<25; i++){
                int valor = (int)(Math.random()*500);
                this.lista.add(valor);
                System.out.println(getName() + " Dato: "+valor);

                if (lista.size() % 5 == 0){
                    synchronized (lista) {
                        lista.notify();
                    }
                }

                try {
                    sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        
    }
}
