class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.travels = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkins:
            self.checkins[id] = []
        
        self.checkins[id].extend([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        diff = t - self.checkins[id][1]
        if self.checkins[id][0] not in self.travels:
            self.travels[self.checkins[id][0]] = {}
        
        if stationName not in self.travels[self.checkins[id][0]]:
            self.travels[self.checkins[id][0]][stationName] = [0, 0]
        
        self.travels[self.checkins[id][0]][stationName][0] += diff
        self.travels[self.checkins[id][0]][stationName][1] += 1
        del self.checkins[id]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travels[startStation][endStation][0] / self.travels[startStation][endStation][1]
    
# ins = {
#     45: ["layton", 3]
#     32: ["paradise", 8]
#     27: ["leyton": 10]
# }

# travels = {
#     "layton": {"waterloo": [22, 2]}
#     "paradise": {"camb": [14, 1]}
# }


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)