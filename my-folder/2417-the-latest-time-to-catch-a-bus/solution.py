class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        
        # bus[i] = departure time of bus
        # pass[j] = arrival time of pass
        # capacity
        
        buses.sort()
        passengers.sort()
        j = 0
        available_slot = 0
        last_bus_full = False
        for i in range(len(buses)):
            capacity_per_bus = capacity
            while j < len(passengers) and passengers[j] <= buses[i] and capacity_per_bus>0:
                j += 1
                capacity_per_bus -= 1
            
            if i == len(buses)-1:
                if capacity_per_bus == 0:
                    last_bus_full = True
                
        
        if last_bus_full == False:
            available_slot = buses[-1]
        else:
            available_slot = passengers[j-1]
        
        for time in range(available_slot, -1, -1):
            if not time in passengers:
                return time
            
        
