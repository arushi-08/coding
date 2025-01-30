class BoundedBlockingQueue {
    private int size;
    private Queue<Integer> queue;

    public BoundedBlockingQueue(int capacity) {
        this.size = capacity;
        this.queue = new LinkedList<>();
    }
    
    public synchronized void enqueue(int element) throws InterruptedException {
        while (this.queue.size() == this.size){
            wait();
        }
        this.queue.offer(element);
        notifyAll();
    }
    
    public synchronized int dequeue() throws InterruptedException {
        while (this.queue.isEmpty()){
            wait();
        }
        int element = this.queue.poll();
        notifyAll();
        return element;
    }
    
    public int size() {
        return this.queue.size();
    }
}
