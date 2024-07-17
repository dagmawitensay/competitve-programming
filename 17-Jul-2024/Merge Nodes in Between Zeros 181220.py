# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        head = head.next
        node_head = head
        curr_node = head

        if not head:
            return None
        
        
        while curr_node:
            path_sum = 0
            while curr_node.val != 0:
                path_sum += curr_node.val
                curr_node = curr_node.next
            
            curr_node = curr_node.next
            head.val = path_sum
            head.next = curr_node
            head = curr_node
        
        return node_head