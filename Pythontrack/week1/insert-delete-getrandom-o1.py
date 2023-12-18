class RandomizedSet:

    def __init__(self):
        self.vals_index = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.vals_index:
            return False
        self.vals.append(val)
        self.vals_index[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals_index:
            return False
        
        last_val = self.vals[-1]
        self.vals[-1], self.vals[self.vals_index[val]] = self.vals[self.vals_index[val]], self.vals[-1]
        self.vals_index[val], self.vals_index[last_val] = self.vals_index[last_val], self.vals_index[val]
        del self.vals_index[val]
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)

# 1, 2
# 1:1, 2:


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()