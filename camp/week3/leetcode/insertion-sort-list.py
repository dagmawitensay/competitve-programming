# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        pointer = head

        while pointer:
            prev = None
            first = dummy
            while first and first.val < pointer.val:
                prev = first
                first = first.next
        
            nextPart = prev.next
            prev.next = ListNode(pointer.val)
            prev = prev.next
            prev.next = nextPart
            pointer = pointer.next
        
        return dummy.next