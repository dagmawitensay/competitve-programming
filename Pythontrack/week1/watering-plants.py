class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        jar = capacity
        steps = 0
        
        for i in range(len(plants)):
            if plants[i] <= jar:
                jar -= plants[i]
                steps += 1
            else:
                jar = capacity
                jar -= plants[i]
                steps += (2 * i + 1)
        
        return steps
                