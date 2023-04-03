public class App {
    public static void main(String[] args) {
        for(int i=0; i<=5; i++){
            Hilo hilo = new Hilo("Thread-"+i);
            hilo.start();
        }
    }
}
