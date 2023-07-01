# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        dummy = head
        dummy2 = head
        while dummy:
            temp.append(dummy.val)
            dummy = dummy.next
        
        for i in range(1, len(temp)):
            k = i
            for j in range(i - 1, -1 , -1):
                if temp[k] < temp[j]:
                    temp[k], temp[j] = temp[j], temp[k]
                k -= 1
        
        i = 0
        while dummy2:
            dummy2.val = temp[i]
            dummy2 = dummy2.next
            i += 1
        
        return head


               