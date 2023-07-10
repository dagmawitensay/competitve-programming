class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        first, second = 0, 0
        pairs = 0
        
        while first < len(players) and second < len(trainers):
            if players[first] <= trainers[second]:
                pairs += 1
                first += 1
                second += 1
            else:
                second += 1
        
        return pairs