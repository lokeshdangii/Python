class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if self.head:
            self.head.prev = node
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def print_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <--> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <--> '
            itr = itr.prev
        print(llstr)


# main function
if __name__ == '__main__':

    dll = DoublyLinkedList()

    dll.insert_at_beginning(10)
    dll.insert_at_beginning(8)
    dll.insert_at_beginning(6)
    dll.insert_at_beginning(4)    
    dll.insert_at_beginning(2)

    dll.insert_at_end(12)
    dll.insert_at_end(14)
    dll.insert_at_end(16)

    print("--------------- Linked List print in forward ---------")
    dll.print_forward()

    print("\n--------------- Linked List print in backwar ---------")
    dll.print_backward()


