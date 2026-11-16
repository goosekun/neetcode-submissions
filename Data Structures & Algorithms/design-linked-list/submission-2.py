class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1
        
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        temp = self.head
        self.head.prev = new_node
        new_node.next = temp
        self.head = new_node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        temp = self.tail
        self.tail.next = new_node
        new_node.prev = temp
        self.tail = new_node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return

        if index > self.size:
            return

        if index <= 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)

        i = 0
        curr = self.head
        prev = None
        while curr and i < index:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = new_node
        new_node.prev = prev
        new_node.next = curr
        curr.prev = new_node
        self.size += 1

        return 


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            
            self.size -= 1

        i = 0
        curr = self.head
        while curr and i < index:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next

        if curr.next:
            curr.next.prev = prev
        else: 
            self.tail = prev

        self.size -= 1
        return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)