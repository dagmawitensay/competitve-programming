class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = 0
        second = 0
        output = []
        
        while first < m and second < n:
            if nums1[first] < nums2[second]:
                output.append(nums1[first])
                first += 1
            else:
                output.append(nums2[second])
                second += 1
            
        while first < m:
            output.append(nums1[first])
            first += 1
        
        while second < n:
            output.append(nums2[second])
            second += 1
        
        for i in range(len(output)):
            nums1[i] = output[i]
            
        