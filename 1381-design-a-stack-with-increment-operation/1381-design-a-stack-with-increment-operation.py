class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            

    def pop(self) -> int:
        if self.stack:
            val = self.stack.pop()
            return val
        
        return -1

    def increment(self, k: int, val: int) -> None:
        bound = min(k, len(self.stack))
        for i in range(bound):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)