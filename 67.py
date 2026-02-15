def fibonacci(n):
    if n <= 1:
        return n
    print(f"fib({n-1}) + fib({n-2})")
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Head = ListNode(1)
A = ListNode(2)
B = ListNode(3)
C = ListNode(4)
Head.next = A
A.next = B
B.next = C
    
def reverse_list(head):
    if not head:
        return
    
    reverse_list(head.next)
    print(head.val)

reverse_list(Head)