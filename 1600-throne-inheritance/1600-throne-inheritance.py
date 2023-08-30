class ThroneInheritance:

    def __init__(self, kingName: str):
        self.adj = defaultdict(list)
        self.kingName = kingName
        self.deaths = set()
        self.order = []

    def birth(self, parentName: str, childName: str) -> None:
        self.adj[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        self.dfs(self.kingName)
        ans = self.order[:]
        self.order = []
        return ans
        
    def dfs(self, name):
        if name not in self.deaths:
            self.order.append(name)
        if not self.adj[name]:
            return
        
        for child in self.adj[name]:
            self.dfs(child)
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()