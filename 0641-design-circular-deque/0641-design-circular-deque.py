class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.queue.insert(0, value)
            return True
        
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            return True
        
        return False
        
    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.queue.pop()
            return True
        
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.queue[0]
        
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.queue[-1]
        
        return -1

    def isEmpty(self) -> bool:
        return self.queue == []
        
    def isFull(self) -> bool:
        return len(self.queue) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()