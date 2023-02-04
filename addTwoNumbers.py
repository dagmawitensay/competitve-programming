# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNum = ''
        secondNum = ''
        while l1:
            firstNum += str(l1.val)
            l1 = l1.next
        while l2:
            secondNum += str(l2.val)
            l2 = l2.next
        print(firstNum,secondNum)
        result = str(int(firstNum[::-1] ) + int(secondNum[::-1]))[::-1]
        l3 = ListNode(result[0])
        l4 = l3
        for i in result[1:]:
            l3.next = ListNode(i)
            l3 = l3.next
        return l4