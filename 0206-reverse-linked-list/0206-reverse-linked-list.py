# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        store = []
        while temp1:
            store.append(temp1.val)
            temp1 = temp1.next
        for i in store[::-1]:
            temp2.val = i
            temp2 = temp2.next
        return head
        