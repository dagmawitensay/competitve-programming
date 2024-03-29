# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        final.next = head
        prev = final
        while head:
            if (head.next) and (head.val == head.next.val):
                while ((head.next) and (head.val == head.next.val)):
                    head = head.next
                prev.next = head.next
                head = head.next
            else:
                prev = prev.next
                head = head.next
        return final.next

        