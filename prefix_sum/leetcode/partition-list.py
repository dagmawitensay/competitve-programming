# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-101)
        dummy2 = ListNode(-101)
        less_than_x = dummy1
        greater_than_x = dummy2

        while head:
            if head.val < x:
                dummy1.next = head
                dummy1 = dummy1.next
            else:
                dummy2.next = head
                dummy2 = dummy2.next
            
            head = head.next
        
        dummy1.next = greater_than_x.next
        dummy2.next = None

        return less_than_x.next