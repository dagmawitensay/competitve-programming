# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        store = []
        if left == right:
            return head
        
        while temp1:
            store.append(temp1.val)
            temp1 = temp1.next
        
        store[left - 1: right] = store[left - 1: right][::-1]
        for value in store:
            temp2.val = value
            temp2 = temp2.next

        return head
