class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        position = {}
        min_length = float('inf')
        
        for end in range(len(cards)):
            if cards[end] in position:
                min_length = min(min_length, end - position[cards[end]] + 1)
            position[cards[end]] = end
        
        return min_length if min_length != float('inf') else -1