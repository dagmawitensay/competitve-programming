class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {v: i for i, v in enumerate(order)}
        status = False

        for i in range(1, len(words)):
            if words[i][0] == words[i - 1][0]:
                j = 0
                while j < len(words[i - 1]) and j < len(words[i]):
                    if alphabet[words[i - 1][j]] != alphabet[words[i][j]]:
                        status = True
                        if alphabet[words[i - 1][j]] > alphabet[words[i][j]]:
                            return False
                        break
                    j += 1
                if len(words[i - 1]) > len(words[i]) and not status:
                    return False
            elif alphabet[words[i - 1][0]] > alphabet[words[i][0]]:
                return False

        return True