# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []
        dummy1 = head
        dummy2 = head
        while dummy1:
            temp.append(dummy1.val)
            dummy1 = dummy1.next
        
        if temp == [] or len(temp) == 1:
            return head
        
        k = k % len(temp)
        
        for i in range(k):
            temp = [temp[-1]] + temp[:-1]
        
        i = 0
        while dummy2:
            dummy2.val = temp[i]
            dummy2 = dummy2.next
            i += 1
            
        return head