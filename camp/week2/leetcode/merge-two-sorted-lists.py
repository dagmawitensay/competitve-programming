# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(first, second, merged):
            if (not first) and second:
                merged.next = second
                return helper(first, second.next, merged.next)
            elif first and (not second):
                merged.next = first
                return helper(first.next, second, merged.next)
            elif (not first) and (not second):
                return merged

            if first.val > second.val:
                merged.next = second
                return helper(first, second.next, merged.next)
            else:
                merged.next = first
                return helper(first.next, second, merged.next)
            
        dummy = ListNode()
        helper(list1, list2, dummy)
        return dummy.next