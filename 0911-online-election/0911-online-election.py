class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leaders = []
        res = defaultdict(int)
        leader = 0
        
        for index, person in enumerate(self.persons):
            res[person] += 1
            if res[person] >= res[leader]:
                leader = person
            self.leaders.append(leader)
        
        
    def search(self, t):
        l, r = 0, len(self.persons) - 1
        res = - 1
        
        while l <= r:
            mid = (l + r) // 2
            if self.times[mid] < t:
                res = max(res, mid)
                l = mid + 1
            elif self.times[mid] > t:
                r = mid - 1
            else:
                return mid
        
        return res
                
    def q(self, t: int) -> int:
        index = self.search(t)
        
        return self.leaders[index]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)