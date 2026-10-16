class ListNode:
    def __init__(self, val: int = 0, nextNode: Optional['ListNode'] = None):
        self.val = val
        self.next = nextNode

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0) # sentinel node

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index+1):
            curr = curr.next
            if curr is None:
                return -1
            if i == index:
                return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        oldHead = self.head.next
        self.head.next = ListNode(val, oldHead)


    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next != None:
            curr = curr.next
        toAdd = ListNode(val)
        curr.next = toAdd
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head # sentinel node, -1 index
        for i in range(index+1):
            curr = curr.next # curr is now at index i
            if curr is None:
                return
            if i == index-1:
                oldNext = curr.next
                toAdd = ListNode(val, oldNext)
                curr.next = toAdd
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head # sentinel node, -1 index
        for i in range(index+1):
            curr = curr.next # curr is now at index i
            if curr is None:
                return
            if i == index-1: # we are right before the node that we want to delete
                if curr.next is None:
                    return
                curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)