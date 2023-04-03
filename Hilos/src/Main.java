public class Main {
    public static void main(String[] args) {
        for(int i=0; i<=5; i++){
            HiloImp hiloImp = new HiloImp("Thread-"+i);
            Thread hilo = new Thread(hiloImp);
            hilo.start();
        }
    }
}
