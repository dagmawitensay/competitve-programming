class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        all_players = set()
        winners = []
        one_losers = []

        for winner, loser in matches:
            losers[loser] = losers.get(loser, 0) + 1
            all_players.add(loser)
            all_players.add(winner)
        
        for player in all_players:
            if player not in losers:
                winners.append(player)
            elif losers[player] == 1:
                one_losers.append(player)
        
        return [sorted(winners), sorted(one_losers)]