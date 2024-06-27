class UndergroundSystem:

    def __init__(self):
        self.station = {}
        self.customertravelstart = {}
        self.journeys = 0

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customertravelstart[id] = {'station':stationName, 'time':t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstation = self.customertravelstart[id]['station']
        starttime = self.customertravelstart[id]['time']
        if startstation not in self.station:
            self.station[startstation] = {}
        if stationName not in self.station[startstation]:
            self.station[startstation][stationName] = (1, t - starttime)
        else:
            journeys, totaltime = self.station[self.customertravelstart[id]['station']][stationName]
            self.station[startstation][stationName] = (journeys + 1 , totaltime + t - starttime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        journeys, totaltime = self.station[startStation][endStation]
        return totaltime/journeys


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
