class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize current node to dummy head of the returning linked list.
        dummy_head = ListNode(0)
        p, q, current = l1, l2, dummy_head
        carry = 0  # Initialize the carry 
        while p is not None or q is not None:
            # At the start of each iteration, we should add carry from last iteration (0 at the start)
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum_ = carry + x + y
            
            # update carry for next calculation
            carry = sum_ // 10
            
            # update the result list.
            current.next = ListNode(sum_ % 10)
            current = current.next
            
            if p is not None: p = p.next
            if q is not None: q = q.next
        
        # check if carry could be added as a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy_head.next