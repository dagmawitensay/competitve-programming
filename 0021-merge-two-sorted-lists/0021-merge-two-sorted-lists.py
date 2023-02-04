# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = []
        while list1:
            temp1.append(list1.val)
            list1 = list1.next
        while list2:
            temp1.append(list2.val)
            list2 = list2.next
        temp1.sort()
        if temp1 == []:
            return
        newList = ListNode(temp1[0])
        final = newList
        for i in temp1[1:]:
            newList.next = ListNode(i)
            newList = newList.next
        return final
        
            