# Linked List implementation
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head= Node(data,None)
            return

        # iterator
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head   #iterator

        ll_str = ""
        while itr:
            ll_str += str(itr.data) + "-->"
            itr = itr.next
            # print(ll_str)

        print(ll_str)

    
    # Length function
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # insert at specific position (index)
    def insert_at(self,index,data):
        
        if index<0 or index > self.get_length():
            raise Exception('--------------- Invalid Index --------------')

        count = 0
        itr = self.head

        while itr:

            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self,value,data):
        itr = self.head

        while itr:

            if itr.data == value:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next

        print("Value not found ")

    # function to remove node from specific position
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("------- Invalid Index ------------")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head

        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    # remove by value
    def remove_by_value(self,value):
        itr = self.head

        # Special case for removing the head node
        if itr and itr.data == value:
            self.head = itr.next
            return

        while itr.next:

            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next
        
    
# main function
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.insert_at_end(60)
    # ll.insert_after_value(5,0)
    ll.remove_by_value(5)
    # ll.insert_at(3,2000)
    # ll.insert_at(4,4000)
    # ll.insert_at(5,6000)
    # ll.remove_at(3)
    # ll.remove_at(3)
    # ll.insert_at(15,8000) 
    ll.print()


# Task
# insert after value
# remove by value