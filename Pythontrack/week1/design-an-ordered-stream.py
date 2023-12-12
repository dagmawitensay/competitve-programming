class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n + 1) 
        self.lookup = set()

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        self.lookup.add(idKey)
        ans = []

        for i in range(1, idKey):
            if i not in self.lookup and idKey != 1:
                return []

        while idKey in self.lookup:
            ans.append(self.stream[idKey])
            idKey += 1
        
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
