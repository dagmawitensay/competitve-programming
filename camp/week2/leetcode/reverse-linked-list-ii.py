# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head

        dummy = ListNode(-501)
        startNode = None
        pointer = head

        for i in range(left - 1):
            startNode = pointer
            pointer = pointer.next
        
        dummy = pointer
        prev = None
        length = right - left

        while dummy and length >= 0:
            nextNode = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = nextNode
            length -= 1
        

        if startNode:
            startNode.next = prev
        else:
            head = prev
            
        pointer.next = dummy

        return head