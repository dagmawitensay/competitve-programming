# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        size = 0
        first = head
        pointer = head

        while first:
            size += 1
            first = first.next
        
        if size <= k:
            length = 1
            extra = 0
        else:
            length = size // k
            extra = size % k
        
        for i in range(k):
            if pointer:
                start = pointer
                for i in range(length - 1):
                    if pointer:
                        pointer = pointer.next
                
                if extra:
                    pointer = pointer.next
                    extra -= 1
                
                nextPart = pointer.next
                pointer.next = None
                pointer = nextPart
                ans.append(start) 
            else:
                ans.append(None)
            
        return ans