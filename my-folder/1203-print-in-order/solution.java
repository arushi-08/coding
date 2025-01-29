import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.*;
class Foo {
    private Semaphore first_sema;
    private Semaphore second_sema;
    private Semaphore third_sema;

    public Foo() {
        this.first_sema = new Semaphore(1);
        this.second_sema = new Semaphore(0);
        this.third_sema = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        this.first_sema.acquire();
        printFirst.run();
        this.first_sema.release();
        this.second_sema.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        this.second_sema.acquire();
        printSecond.run();
        this.third_sema.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        
        // printThird.run() outputs "third". Do not change or remove this line.
        this.third_sema.acquire();
        printThird.run();
        this.third_sema.release();
    }
}
