class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                ans += 'G'
            elif command[i] == '(':
                count = 1
                i += 1
                while i < len(command) and command[i] != ')':
                    count += 1
                    i += 1
                if count > 1:
                    ans += 'al'
                else:
                    ans += 'o'
            
            i += 1
        
        return ans