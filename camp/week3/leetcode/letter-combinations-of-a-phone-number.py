class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q','r','s'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        ans = []
        curr = []
        def backtrack(index):
            if len(curr) == len(digits):
                result = "".join(curr)
                if result:
                    ans.append(result)
                return

            if index >= len(digits):
                return
            
            for i in range(index, len(digits)):
                for val in store[digits[index]]:
                    curr.append(val)
                    backtrack(i + 1)
                    curr.pop()
        
        backtrack(0)
        return ans