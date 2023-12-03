class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        store = {str(i): i for i in range(10)}
        val1 = 0
        val2 = 0
        for i in range(len(num1)):
            val1 = val1 * 10 + store[num1[i]]
        
        for i in range(len(num2)):
            val2 = val2 * 10 + store[num2[i]]

        return str(val1 * val2)