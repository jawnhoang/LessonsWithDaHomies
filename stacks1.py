class Stack:
    #private variables
    def __init__(self):
        self.stackArr = [] #stack is created

    def push(self, number): #push the newest number into stack
        self.stackArr.insert(0, number)

    def pop(self): #remove top number (last added) from stack
        return self.stackArr.pop(0)

    def top(self): #what is the number at the top of stack
        return self.stackArr[0]

    def size(self): #find size of stack
        return len(self.stackArr)

if __name__=='__main__':
    myStack = Stack() #declare stack class object

    #push elements into stack
    myStack.push(10)
    myStack.push(12)
    myStack.push(50)
    myStack.push(100)

    #pop stack elements and print
    size = myStack.size() #find size to run for loop
    for i in range(size):
        print(myStack.pop())

    print('pog')
