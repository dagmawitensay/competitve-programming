class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurences = {char: i for i, char in enumerate(s)}
        end, size = 0, 0
        ans = []

        for i in range(len(s)):
            size += 1
            end = max(end, last_occurences[s[i]])

            if i == end:
                ans.append(size)
                size = 0
        
        return ans