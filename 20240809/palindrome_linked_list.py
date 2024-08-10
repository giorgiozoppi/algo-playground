from typing import Optional

class ListNode:
    def __init__(self, val: int=0, next=None) -> None:
         self.val: int = val
         self.next = next

class Solution:
    def reverseList(self, slow_ptr: ListNode) -> ListNode:
        next_node = None
        curr = slow_ptr
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def equalList(self, firstHead: ListNode, secondHead: ListNode) -> bool:
        firstListCurrent, secondListCurrent = firstHead, secondHead
        while firstListCurrent and secondListCurrent:
            if firstListCurrent.val != secondListCurrent.val:
                return False    
            firstListCurrent = firstListCurrent.next
            secondListCurrent = secondListCurrent.next
        
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        reverted_data = self.reverseList(slow_pointer)
        return self.equalList(head, reverted_data)
        