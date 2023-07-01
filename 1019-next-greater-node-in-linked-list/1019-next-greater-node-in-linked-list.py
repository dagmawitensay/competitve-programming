# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp = []
        
        while head:
            temp.append(head.val)
            head = head.next
            
        result = [0] * len(temp)
        stack = []
        for i, value in enumerate(temp):
            while stack and temp[stack[-1]] < value:
                smaller = stack.pop()
                result[smaller] = value
            
            stack.append(i)
            
    
        return result
            
        