# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # both lists have elements
        out = None
        curr = None
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                if curr is None:
                    curr = list1
                    out = curr
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if curr is None:
                    curr = list2
                    out = curr
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
        # only one list has elements
        # if list 1 has no elements left
        if list1 is None:
            if curr is None:
                curr = list2
                out = curr
            else:
                curr.next = list2
        # if list 2 has no elements left
        else:
            if curr is None:
                curr = list1
                out = curr
            else:
                curr.next = list1
        return out