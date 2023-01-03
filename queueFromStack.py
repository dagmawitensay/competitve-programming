class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0
    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2 = []
        for i in self.stack1[::-1]:
            self.stack2.append(i)
        self.size += 1
    def pop(self) -> int:
        value = self.peek()
        self.stack2.pop()
        self.stack1 = []
        for i in self.stack2[::-1]:
            self.stack1.append(i)
        self.size -= 1
        return value
    def peek(self) -> int:
        return self.stack2[self.size - 1]
    def empty(self) -> bool:
        return self.stack2 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()