# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
            
        odd_nodes = head
        even_nodes = head.next
        list2 = even_nodes

        while even_nodes and even_nodes.next:
            odd_nodes.next = even_nodes.next
            odd_nodes = odd_nodes.next

            even_nodes.next = odd_nodes.next
            even_nodes = even_nodes.next
        
        odd_nodes.next = list2

        return head