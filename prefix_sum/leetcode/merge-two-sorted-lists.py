# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currNode = dummy = ListNode()
        first, second = list1, list2

        while first and second:
            if first.val <= second.val:
                currNode.next = first
                currNode = currNode.next
                first = first.next
            else:
                currNode.next = second
                currNode = currNode.next
                second = second.next
        
        while first:
            currNode.next = first
            currNode = currNode.next
            first = first.next
        
        while second:
            currNode.next = second
            currNode = currNode.next
            second = second.next
        
        return dummy.next

                
