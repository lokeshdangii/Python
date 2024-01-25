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