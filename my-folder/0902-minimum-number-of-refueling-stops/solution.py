class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # method 2: greedy + heap

        stations.sort(key=lambda x:x[0])
        # see if travel_so_far + startFuel is taking up to stations
        travel_so_far = 0
        fuels = []
        minsteps = 0 
        current_fuel = startFuel

        for pos, fuel in stations:
            if travel_so_far + current_fuel >= target:
                return minsteps
            fuel_to_use = 0
            dist = pos - travel_so_far
            while current_fuel < min(dist, target):
                if not fuels:
                    return -1
                current_fuel += -heappop(fuels)
                minsteps += 1
            
            travel_so_far = pos
            current_fuel -= dist
            heappush(fuels, -fuel)
        
        
        dist = target - travel_so_far
        while current_fuel < dist:
            if not fuels:
                return -1
            
            current_fuel += -heappop(fuels)
            minsteps += 1
        
        return minsteps
        
                    
