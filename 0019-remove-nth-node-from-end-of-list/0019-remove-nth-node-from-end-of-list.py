# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head1 = head
        head2 = head
        len = 0
        if not head.next:
            head = None
            return head
        while head1:
            len += 1
            head1 = head1.next
        if len == n:
            head = head.next
            return head
        for i in range(len - n -1):
            head2 = head2.next
        head2.next = head2.next.next
       
        return head
