# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = ListNode(-101)
        node = head

        while node:
            if prevNode.val == node.val:
                while node and prevNode.val == node.val:
                    node = node.next
                
                prevNode.next = node
            prevNode = node
            if node:
                node = node.next
        
        return head