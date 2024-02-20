class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, index):
            if index == len(s) // 2:
                return
            
            s[index], s[len(s) - 1 - index] = s[len(s) - 1 - index], s[index]
            helper(s, index + 1)
        
        helper(s, 0)