# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        max_twin_sum = 0
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
            if fast:
                fast = fast.next
        
        curr = slow
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev  = curr
            curr = next
        
        slow = prev
        
        while slow:
            val = head.val + slow.val
            max_twin_sum = max(max_twin_sum, val)
            head = head.next
            slow = slow.next
        
        return max_twin_sum
        
        