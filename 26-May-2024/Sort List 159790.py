# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp, temp2 = head, head
        store = []
        
        while temp:
            store.append(temp.val)
            temp = temp.next
        
        def mergeSort(array):
            if len(array) > 1:
                left = array[:len(array) // 2]
                right = array[len(array) // 2:]
                mergeSort(left)
                mergeSort(right)
                
                merge(left, right, array)
        
        def merge(arr1, arr2, temp):
            current1 = 0
            current2 = 0
            current3 = 0
            while current1 < len(arr1) and current2 < len(arr2):
                if arr1[current1] < arr2[current2]:
                    temp[current3]  = arr1[current1]
                    current1 += 1
                    current3 += 1
                else:
                    temp[current3] = arr2[current2]
                    current2 += 1
                    current3 += 1
            
            while current1 < len(arr1):
                temp[current3] = arr1[current1]
                current1 += 1
                current3 += 1
            
            while current2 < len(arr2):
                temp[current3] = arr2[current2]
                current2 += 1
                current3 += 1
        
        mergeSort(store)
        
        i = 0
        while temp2:
            temp2.val = store[i]
            i += 1
            temp2 = temp2.next
    
        
        return head