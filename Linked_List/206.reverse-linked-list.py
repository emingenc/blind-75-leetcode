from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
        

""" Here is the explanation for the code above:
1. We declare a variable pre and assign it to None.
2. We declare a variable cur and assign it to head.
3. We iterate until cur is not None.
4. Then we declare a variable next and assign it to cur.next.
5. Then we assign cur.next to pre.
6. Then we assign pre to cur.
7. Then we assign cur to next. """
        
