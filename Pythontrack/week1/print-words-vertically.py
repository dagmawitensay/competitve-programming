class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        i = 0
        s = s.split()
        longest = max(s, key=len)
        for i in range(len(longest)):
            curr_str = ""
            for word in s:
                if i < len(word):
                    curr_str += word[i]
                else:
                    curr_str += " "
            if curr_str:
                ans.append(curr_str.rstrip())
            
        return ans