import java.util.concurrent.Semaphore;
class H2O {
    private Semaphore hyd_sema;
    private Semaphore oxy_sema;
    private int count;
    private final Object lock = new Object();

    public H2O() {
        this.hyd_sema = new Semaphore(1);
        this.oxy_sema = new Semaphore(0);
        this.count = 0;
        
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        this.hyd_sema.acquire();
        releaseHydrogen.run();
        synchronized(lock){ 
            this.count += 1;
            if (this.count == 2){
                this.oxy_sema.release();
                this.count = 0;
            } else{
                this.hyd_sema.release();
            }
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
        this.oxy_sema.acquire();
		releaseOxygen.run();
        this.hyd_sema.release();
    }
}
