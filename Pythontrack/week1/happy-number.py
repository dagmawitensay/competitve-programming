class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            temp = 0
            print(n)
            while n > 0:
                temp += (n % 10) ** 2
                n //= 10
            n = temp
        
        if n == 1:
            return True
        
        return False
