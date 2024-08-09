from typing import Optional
class ListNode:
    def __init__(self, val: int) -> int:
        self.val = val
        self.next = None
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        left = head
        
        while right and n > 0: 
            right = right.next
            n = n - 1
        # the list shorter than n
        prev = head
        left = head 
        if n == 0:
            while right:
                prev = left
                left = left.next
                right = right.next
            
            if left == head and prev == head:
                head = head.next
                return head
            else:
                prev.next = left.next
            
        else:
            return None
        return head
