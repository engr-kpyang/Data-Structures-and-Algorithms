# Queue Data structure

class Queue:
    def __init__(self) -> None:
        self.queue  = []
    
    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    #Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display the queue
    def displayQueue(self):
        print(self.queue)

    def queueSize(self):
        return len(self.queue)

    
newQueue = Queue()

newQueue.enqueue(47)
newQueue.enqueue(99)
newQueue.displayQueue()
newQueue.enqueue(48)
newQueue.enqueue(32)
newQueue.displayQueue()
newQueue.dequeue()
newQueue.dequeue()
newQueue.displayQueue()


