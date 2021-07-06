class Queue:
    def __init__(self):
        self.myQ = [] #queue array created

    def enqueue(self, number):
        self.myQ.insert(0,number)

    def dequeue(self):
        return self.myQ.pop()

    def size(self):
        return len(self.myQ)

if __name__ == '__main__':
    myQ = Queue() #create queue object

    
    myQ.enqueue(10)
    myQ.enqueue(12)
    myQ.enqueue(50)
    myQ.enqueue(100)

    size = myQ.size()
    for i in range(size):
        print(myQ.dequeue())
