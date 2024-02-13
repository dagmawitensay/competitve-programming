# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        currNode = head
        if not head or not head.next:
            return

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        while currNode and slow:
            if currNode == slow:
                return currNode
            
            currNode = currNode.next
            slow = slow.next























