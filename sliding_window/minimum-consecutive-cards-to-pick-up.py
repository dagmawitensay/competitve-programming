class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        visited = set()
        start = 0
        longest = float('inf')

        for end in range(len(cards)):
            while cards[end] in visited:
                longest = min(longest, end - start + 1)
                visited.remove(cards[start])
                start += 1
            
            visited.add(cards[end])
        
        return longest if longest != float('inf') else -1
