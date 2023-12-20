class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0

        for i in range(len(strs[0])):
            prev = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] < prev:
                    count += 1
                    break
                else:
                    prev = strs[j][i]
        
        return count
