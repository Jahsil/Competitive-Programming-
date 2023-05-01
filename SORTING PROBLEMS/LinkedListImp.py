class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self , value):
        if(self.head == None):
            new_Node = Node(value)
            self.head = new_Node

        new_Node = Node(value)
        new_Node.next = self.head
        self.head = new_Node

    def insertAfter(self , prevNode , value):
        if (prevNode == None):
            print("no previous node")
        new_Node = Node(value)
        new_Node.next = prevNode.next
        prevNode.next = new_Node

    def append(self , value):
        new_Node = Node(value)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_Node



    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    #
    # list = LinkedList()
    # list.head = Node(1)
    # second = Node(2)
    # third = Node(3)
    #
    # list.head.next = second
    # second.next = third
    #
    # list.push(5)
    # list.push(6)
    #
    # list.insertAfter(second,10)
    #
    # list.append(9)
    #
    # list.printList()
    sum = 95
    print(sum%10)
    carry = sum //10
    print(carry)










