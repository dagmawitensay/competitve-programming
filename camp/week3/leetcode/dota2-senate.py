class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dir = deque()

        for i, char in enumerate(senate):
            if char == 'R':
                rad.append(i)
            else:
                dir.append(i)
        
        while len(rad) > 0 and len(dir) > 0:
            r = rad.popleft()
            d = dir.popleft()
            if r < d:
                rad.append(r + len(senate))
            else:
                dir.append(d + len(senate))
        
        return 'Dire' if len(dir) > 0 else 'Radiant'