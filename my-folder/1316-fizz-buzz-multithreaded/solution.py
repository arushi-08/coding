import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 0
        self.lock = threading.Lock()
        self.num_lock = threading.Semaphore(1)
        self.fizz_lock = threading.Semaphore(0)
        self.buzz_lock = threading.Semaphore(0)
        self.fizzbuzz_lock = threading.Semaphore(0)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fizz_lock.acquire()
            if self.i == self.n:
                break
            printFizz()
            self.num_lock.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.buzz_lock.acquire()
            if self.i == self.n:
                break
            printBuzz()
            self.num_lock.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fizzbuzz_lock.acquire()
            if self.i == self.n:
                break
            printFizzBuzz()
            self.num_lock.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(1, self.n + 1):
            self.num_lock.acquire()
            
            if i % 15 == 0:
                self.fizzbuzz_lock.release()
            elif i % 3 == 0:
                self.fizz_lock.release()
            elif i % 5 == 0:
                self.buzz_lock.release()
            else:
                # Print a normal number => release num_lock here
                printNumber(i)
                self.num_lock.release()

        self.num_lock.acquire()
        self.i = self.n
        self.num_lock.release()
        self.fizz_lock.release()
        self.buzz_lock.release()
        self.fizzbuzz_lock.release()

