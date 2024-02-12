# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prev = None

        while currNode:
            nextNode = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = nextNode
        
        return prev
