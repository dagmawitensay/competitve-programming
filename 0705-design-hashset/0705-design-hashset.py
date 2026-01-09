class MyHashSet:

    def __init__(self):
        self.hash = set()
        

    def add(self, key: int) -> None:
        self.hash.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)
        

    def contains(self, key: int) -> bool:
        return True if key in self.hash else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)