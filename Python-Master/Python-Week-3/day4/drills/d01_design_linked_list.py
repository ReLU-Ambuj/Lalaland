# Drill 1: Design Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        curr = self.head
        for _ in range(index): curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.size += 1

    def printList(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(res))

if __name__ == '__main__':
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtHead(2)
    ll.printList() # 2 -> 1
