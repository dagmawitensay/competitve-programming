# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        unique = set()
        
        while fast:
            unique.add(fast)
            fast = fast.next
            
            if fast in unique:
                return fast
        
        return None