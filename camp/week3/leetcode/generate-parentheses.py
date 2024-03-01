class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        curr = []
        def backtrack(opening, closing):
            if len(curr) == 2 * n:
                combinations.append("".join(curr))
                return
            
            if opening:
                curr.append("(")
                backtrack(opening - 1, closing)
                curr.pop()
            
            if closing > opening:
                curr.append(")")
                backtrack(opening, closing - 1)
                curr.pop()
            
        backtrack(n, n)
        return combinations