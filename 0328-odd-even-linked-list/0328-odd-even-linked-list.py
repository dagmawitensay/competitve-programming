# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = []
        odds = []
        evens = []
        temp = head
        temp2 = head
        while temp:
            store.append(temp.val)
            temp = temp.next
            
        for i in range(len(store)):
            if i % 2 == 0:
                odds.append(store[i])
            else:
                evens.append(store[i])
        odds = odds + evens        
        for i in odds:
            temp2.val = i
            temp2 = temp2.next
        
        return head
            