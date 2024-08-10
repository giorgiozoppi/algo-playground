# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def append(self, head: ListNode, tail: ListNode, value: int)->None:
        if head is None:
            head = ListNode(value)
            tail = head
        else:
            tmp = tail
            tmp.next = ListNode(value)
            tail = tmp.next
        return head, tail
        
    def add(self, node1: ListNode, node2: ListNode, carry: int) -> Tuple[int, int]:
        if node1 and node2:
            temp_sum = node1.val + node2.val + carry
        elif node1 and not node2:
            temp_sum = node1.val + carry
        elif node2 and not node1:
            temp_sum = node2.val + carry
        
        digit = temp_sum - 10 if temp_sum >= 10 else temp_sum
        carry = 1 if temp_sum >= 10 else 0
        return digit, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry: int = 0
        next1: Optional[ListNode] = l1
        next2: Optional[ListNode] = l2
        head, tail = None, None
        digit = 0
        if not l1 and not l2:
            return None
        while next1 or next2:
            if next1 and next2:
                digit, carry = self.add(next1, next2, carry)
                next1 = next1.next 
                next2 = next2.next
            elif next1:
                digit, carry = self.add(next1, next2, carry)
                next1 = next1.next
            else:
                digit, carry = self.add(next1, next2, carry)
                next2 = next2.next
            head, tail = self.append(head, tail, digit)
        if not next1 and not next2 and carry == 1:
            head, tail = self.append(head, tail, carry)
        return head



