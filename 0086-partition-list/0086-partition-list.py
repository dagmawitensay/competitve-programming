# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        temp2 = head
        temp3 = head
        store = []
        smaller = []
        greater = []
        i = 0
        
        while temp:
            store.append(temp.val)
            temp = temp.next
        
        while temp2:
            if temp2.val < x:
                smaller.append(temp2.val)
            else:
                greater.append(temp2.val)
            temp2 = temp2.next            
        
        smaller = smaller + greater
    
        while temp3:
            temp3.val = smaller[i]
            temp3 = temp3.next
            i += 1
        
        return head
        
        
        
        