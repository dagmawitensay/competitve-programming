class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.k = k
        self.size = 0      

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue.append(value)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.queue.pop(0)
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[-1]        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

[2, 3, 4]