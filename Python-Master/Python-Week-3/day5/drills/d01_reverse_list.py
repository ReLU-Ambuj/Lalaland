# Drill 1: Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next # Save next
        curr.next = prev # Reverse pointer
        prev = curr      # Move prev forward
        curr = nxt       # Move curr forward
    return prev # Prev is the new head

def printList(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3)))
    printList(head) # 1 -> 2 -> 3
    new_head = reverseList(head)
    printList(new_head) # 3 -> 2 -> 1
