class CircularQueue():

    def __init__(self, queueSize):
        self.queueSize = queueSize
        self.queue = [None] * queueSize
        self.head = self.tail = -1

    def enqueue(self, data):
        if((self.tail + 1) % self.queueSize == self.head):
            print('The circular queue is full\n')

        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.queueSize
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print('The circular queue is empty\n')
        
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.queueSize
            return temp

    def printQueue(self):
        if(self.head == -1):
            print('No element in the circular queue')

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end= " ")
            print()
        else:
            for i in range(self.head, self.queueSize):
                print(self.queue[i], end=" ")  
            for i in range(0, self.tail + 1):
                print(self.queue[i], end= " ")
            print()

newCQ = CircularQueue(5)
newCQ.enqueue(12)
newCQ.printQueue()
newCQ.enqueue(23)
newCQ.enqueue(34)
newCQ.printQueue()
newCQ.enqueue(45)
newCQ.enqueue(56)
newCQ.printQueue()
newCQ.enqueue(67)
newCQ.printQueue()
newCQ.dequeue()
newCQ.printQueue()
newCQ.dequeue()
newCQ.printQueue()
newCQ.dequeue()
newCQ.printQueue()
newCQ.dequeue()
newCQ.printQueue()
newCQ.dequeue()
newCQ.printQueue()
