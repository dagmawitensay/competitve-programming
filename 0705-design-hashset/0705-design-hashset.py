class MyHashSet:

    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]
        
    def add(self, key: int) -> None:
        bucket = self._getBucket(key)
        if key in bucket:
            return
        
        bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self._getBucket(key)

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self._getBucket(key)
        return key in bucket
    
    def _getHash(self, key):
        return key % self.size
    
    def _getBucket(self, key):
        hash = self._getHash(key)
        return self.buckets[hash]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)