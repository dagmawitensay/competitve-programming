class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and  currentTime < (self.tokens[tokenId] + self.timeToLive):
            self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return len(list(v for k, v in self.tokens.items() if currentTime < (v + self.timeToLive)))
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)