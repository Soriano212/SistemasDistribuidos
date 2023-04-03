public class Hilo extends Thread{
    public Hilo (String string){
        super(string);
    }

    public void run() {
        double sec = 2+(Math.random()*3);
        try {
            sleep((long) sec*1000);
            System.out.println(getName() + " Tiempo: "+sec);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
