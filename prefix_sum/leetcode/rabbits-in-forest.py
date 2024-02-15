class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        rabbits = 0

        for key, count in counts.items():
            same = count // (key + 1)
            rabbits += ((key + 1) * same)
            if count % (key + 1) != 0:
                rabbits += (key + 1)
        
        return rabbits