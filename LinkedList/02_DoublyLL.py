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

    # Length function
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at(self,index,data):
        if index<0 or index > self.get_length():
            raise Exception('--------------- Invalid Index --------------')

        if index == 0:
            self.insert_at_beginning()
            return

        count= 0
        itr = self.head
        
        while itr:

            if count == index-1:
                node = Node(data,itr.next,itr)

                if node.next:
                    node.next.prev = node
                
                itr.next = node
                break

            itr = itr.next
            count += 1

    # function to remove node from specific position
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("------- Invalid Index ------------")

        if index == 0:
            self.head = self.head.next

        count =0
        itr = self.head

        while itr:
            if count == index-1:
                itr.next = itr.next.next
                itr.next.prev = itr.next 
                break

            itr = itr.next
            count += 1


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

    dll.insert_at(3,2000)
    print(dll.get_length())

    dll.remove_at(3)

    print("--------------- Linked List print in forward ---------")
    dll.print_forward()

    print("\n--------------- Linked List print in backwar ---------")
    dll.print_backward()


