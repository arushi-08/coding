class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # car travels east covering target miles
        # gas stations = [pos, fuel]
        # initially startFuel
        # 1 l/mile
        # output: min num of station stops to reach destination
        #   else return -1

        # startFuel -> gas station
        # [10,60],[20,30],[30,30],[60,40]
        # startFuel = 10
        # target = 100

        # 1 -> 60
        # 4 -> 40 - position 60 + 40 = 100

        # car_pos
        # gas_station - 
        # car_fuel

        # car_pos + car_fuel >= desti -> return 0
        # car_pos + car_fuel >= last gas station - binary search
        # car_fuel -= last gas station pos + last gas station fuel

        if startFuel >= target: return 0
        if not stations and startFuel < target: return -1
        car_position = 0
        stations.sort()
        print(stations)
        st = 0
        ed = len(stations)-1

        ans_num_stops = 0
        # if we cannot reach next stop, we stop at a gas stop w max fuel
        heap = []
        i = 0
        while car_position + startFuel < target:  
            while i < len(stations) and car_position + startFuel >= stations[i][0]:
                heappush(heap, (-stations[i][1], stations[i][0])) 
                i += 1
            if not heap: 
                break
            fuel, pos = heappop(heap)
            fuel = -fuel
            startFuel = startFuel - (pos-car_position) + fuel # 25
            car_position = pos # 25
            ans_num_stops += 1 # 1

        if car_position + startFuel >= target:
            return ans_num_stops
        return -1






