# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head1 = head
        # head2 = head
        # size = 0
        # if not head.next:
        #     head = None
        #     return head

        # while head1:
        #     size += 1
        #     head1 = head1.next

        # if size == n:
        #     head = head.next
        #     return head

        # for i in range(size - n -1):
        #     head2 = head2.next

        # head2.next = head2.next.next
       
        # return head

        left = right = head

        for i in range(n):
            right = right.next
        
        if not right:
            return head.next
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return head