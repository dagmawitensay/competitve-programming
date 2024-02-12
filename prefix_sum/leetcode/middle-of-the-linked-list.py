# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        node1 = head
        node2 = head
        
        while node1:
            size += 1
            node1 = node1.next
        
        for i in range(size // 2):
            node2 = node2.next
        
        return node2
