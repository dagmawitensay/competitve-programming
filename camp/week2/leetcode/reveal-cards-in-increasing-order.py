class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque(range(len(deck)))
        result = [0] * len(deck)
        
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        
        return result