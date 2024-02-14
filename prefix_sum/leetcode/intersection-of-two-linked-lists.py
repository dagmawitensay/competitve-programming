# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        size1 = size2 = 0
        first, second = headA, headB

        while first:
            size1 += 1
            first = first.next
        
        while second:
            size2 += 1
            second = second.next
        
        diff = abs(size1 - size2)
        for i in range(diff):
            if size1 > size2:
                headA = headA.next
            else:
                headB = headB.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
