## Palindrome Linked List.
Given the head of a singly linked list, return true if it is a 
palindrome  or false otherwise.
The constrains are O(n) time, and O(n) space.

Some meaniful use cases are:
``
item_a = [1,2,2,1]  => true
item_b = [1,2]  => false
item_c = [1,0,1] => true
item_d = [1,1,2,1] => false
``
To achieve O(n) and most important to achieve O(1) in space you should use the fast/slow pointer techinique.
- Initialize both pointer to head of the list
- Increase fast = fast.next.next, slow = slow.next and loop until fast and fast.next are not None
- When exit from the loop you will find the slow pointer at the middle of the list.
- Now we're in a position to revert the second part of the list.
```
  item_a = [1,2,2,1]
  - slow will point to the first 2
  - fast will piint to the second 2
```
So now you can revert the second part of the list starting from the middle and compare each item with head.
If the comparison is successfully we're a palindrome.

 