from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dire = deque()
        for i, v in enumerate(senate):
            if v == 'R':
                rad.append(i)
            else:
                dire.append(i)
        
        while len(rad) != 0 and len(dire) != 0:
            curr_rad = rad.popleft()
            curr_dire = dire.popleft()
            
            if curr_rad < curr_dire:
                rad.append(curr_rad + len(senate))
            else:
                dire.append(curr_dire + len(senate))
        
        return 'Dire' if len(dire) != 0 else 'Radiant'