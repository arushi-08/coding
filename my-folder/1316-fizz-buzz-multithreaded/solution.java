import java.util.concurrent.Semaphore;
class FizzBuzz {
    private int n;
    private boolean done;
    private Semaphore num_sema;
    private Semaphore fizz_sema;
    private Semaphore buzz_sema;
    private Semaphore fizzbuzz_sema;

    public FizzBuzz(int n) {
        this.n = n;
        num_sema = new Semaphore(1);
        fizz_sema = new Semaphore(0);
        buzz_sema = new Semaphore(0);
        fizzbuzz_sema = new Semaphore(0);
        this.done = false;
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        while (true){
            this.fizz_sema.acquire();
            if (this.done){
                break;
            }
            printFizz.run();
            this.num_sema.release();
        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        while (true){
            this.buzz_sema.acquire();
            if (this.done){
                break;
            }
            printBuzz.run();
            this.num_sema.release();
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (true){
            this.fizzbuzz_sema.acquire();
            if (this.done){
                break;
            }
            printFizzBuzz.run();
            this.num_sema.release();
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        
        for (int i=1; i<this.n+1; i++){
            this.num_sema.acquire();

            if (i % 15 == 0){
                this.fizzbuzz_sema.release();
            }
            else if (i % 3 == 0){
                this.fizz_sema.release();
            }
            else if (i % 5 == 0){
                this.buzz_sema.release();
            }
            else {
                printNumber.accept(i);
                this.num_sema.release();
            }
        }

        this.num_sema.acquire();
        this.done = true;
        this.num_sema.release();
        this.fizzbuzz_sema.release();
        this.fizz_sema.release();
        this.buzz_sema.release();
    }
}
