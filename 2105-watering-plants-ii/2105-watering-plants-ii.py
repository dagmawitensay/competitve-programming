class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants) - 1
        refills = 0
        jarA = capacityA
        jarB = capacityB
        
        def Afill(i):
            nonlocal jarA
            nonlocal refills
            if plants[i] <= jarA:
                jarA -= plants[i]
            else:
                jarA = capacityA
                refills += 1
                jarA -= plants[i]
        
        def Bfill(i):
            nonlocal jarB
            nonlocal refills
            if plants[i] <= jarB:
                jarB -= plants[i]
            else:
                jarB = capacityB
                refills += 1
                
                jarB -= plants[i]
    
            
        
        while l <= r:
            if l == r:
                if jarA == jarB or jarA > jarB:
                    Afill(l)
                else:
                    Bfill(r)
            else:
                Afill(l)
                Bfill(r)
            
            l += 1
            r -= 1
        
        return refills