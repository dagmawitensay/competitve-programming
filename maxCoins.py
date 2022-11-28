def maxCoins(piles):
    index =  len(piles)//3
    piles.sort()
    remaining_piles = piles[index:]
    max_coins = 0
    for i in range(0,len(remaining_piles),2):
        max_coins += remaining_piles[i]
    return max_coins

