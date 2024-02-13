# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        list1, list2 = dummy1, dummy2

        while head:
            dummy1.next = head
            dummy1 = dummy1.next
            head = head.next
            dummy2.next = head
            dummy2 = dummy2.next
            if head:
                head = head.next
        
        dummy1.next = list2.next

        return list1.next