from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        prev = None
        if list1.val < list2.val:
            prev = list1
            list1 = list1.next
        else:
            prev = list2
            list2 = list2.next
        curr = prev
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return prev
        
""" Here is the explanation for the code above:
    1. If list1 is empty, return list2.
    2. If list2 is empty, return list1.
    3. If list1's value is smaller than list2's value,
         set prev to list1 and list1 to list1.next.
    4. If list1's value is larger than list2's value,
            set prev to list2 and list2 to list2.next.
    5. Set curr to prev.
    6. While list1 and list2 are not empty,
            if list1's value is smaller than list2's value,
                set curr.next to list1 and list1 to list1.next.
            else,
                set curr.next to list2 and list2 to list2.next.
            set curr to curr.next.
    7. If list1 is not empty, set curr.next to list1.
    8. If list2 is not empty, set curr.next to list2.
    9. Return prev.
"""
