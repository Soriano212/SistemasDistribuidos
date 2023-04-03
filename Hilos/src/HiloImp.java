public class HiloImp implements Runnable{
    private String name;
    public HiloImp(String name){
        this.name = name;
    }

    public void run() {
        double sec = 2+(Math.random()*3);
        try {
            Thread.sleep((long) sec*1000);
            System.out.println(this.name + " Tiempo: "+sec);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
