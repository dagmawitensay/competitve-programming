# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        middle = len(temp) // 2
        middleNodes = ListNode(temp[middle])
        final = middleNodes
        for i in range(middle + 1, len(temp)):
            middleNodes.next = ListNode(temp[i])
            middleNodes = middleNodes.next
        return final
        