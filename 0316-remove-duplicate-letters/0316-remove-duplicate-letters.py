class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occurence = {}
        visited = set()
        
        for i in range(len(s)):
            last_occurence[s[i]] = i
            
        
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and stack[-1] > s[i] and last_occurence[stack[-1]] > i:
                visited.remove(stack.pop())
            
            stack.append(s[i])
            visited.add(s[i])
        
        return "".join(stack)