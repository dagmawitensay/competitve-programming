class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        for i, value in enumerate(parent):
            self.graph[value].append(i)
        
        self.locks = [0] * len(parent)
        

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] == 0:
            self.locks[num] = user
            return True
        
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == 0 or self.locks[num] != user:
            return False
        
        self.locks[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locks[num] != 0:
            return False
        
        if self.hasLockedAncestor(num):
            return False
        
        if not self.hasLockedDescendant(num):
            return False
        
        self.lockDescendants(num)
        self.locks[num] = user
        return True
     
    def hasLockedAncestor(self, num):
        while num != -1:
            if self.locks[num] != 0:
                return True
            num = self.parent[num]
        
        return False
    
    def hasLockedDescendant(self, num):
        if self.locks[num] != 0:
            return True
        
        for child in self.graph[num]:
            if self.hasLockedDescendant(child):
                return True
        
        return False

    
    def lockDescendants(self, num):
        self.locks[num] = 0
        
        for child in self.graph[num]:
            self.lockDescendants(child)
            
        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)