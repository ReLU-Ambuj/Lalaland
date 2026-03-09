# Linked List Memory Model
A Python reference is just a pointer.
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
**Golden Rule:** NEVER lose the `head`.
When traversing, ALWAYS create a dummy pointer `curr = head` and loop `while curr: curr = curr.next`.
If you write `while head: head = head.next`, you have permanently lost your list!
