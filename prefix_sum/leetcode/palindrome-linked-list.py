# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        store = []
        while temp:
            store.append(temp.val)
            temp = temp.next
        
        if store == store[::-1]:
            return True
        
        return False
            
        