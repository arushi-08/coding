"""goal: group them to form H2O
barrier: each thread has to wait until complete molecule can be formed.
use semaphore 
allow 2 hydrogen - release lock
allow 1 oxygen - release
"""
import threading
class H2O:
    def __init__(self):
        self.hyd_sema = threading.Semaphore(1)
        self.oxy_sema = threading.Semaphore(1)
        self.count = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.hyd_sema.acquire()
        releaseHydrogen()
        self.count += 1
        if self.count == 2:
            self.oxy_sema.release()
            self.count = 0
        else:
            self.hyd_sema.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.oxy_sema.acquire()
        releaseOxygen()
        self.hyd_sema.release()
        
