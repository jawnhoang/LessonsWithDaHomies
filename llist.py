class Node:
    def __init__(self, data):
        self.data = data #initialize first data in node
        self.Next = None #initialize to point to nothing


class LinkedList:
    def __init__(self):
        self.head = None

    #print LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.Next



#main function
if __name__ == '__main__':
    llObj1 = LinkedList() #create linkedlist object

    llObj1.head = Node(1)
    llObj2 = Node(2)
    llObj3 = Node(3)

    llObj1.next = llObj2 #connects node 1 with node 2
    llObj2.next = llObj3      #connect node 2 with node 3

    llObj1.printList()
