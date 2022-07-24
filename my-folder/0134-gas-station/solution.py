class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        
        index = 0
        start_point = index
        Car_tank = 0
        Index_is_at_start = True
        while index < len(gas):
            if index == start_point and Index_is_at_start == False:
                break
            Index_is_at_start = False
            if Car_tank > 0:
                Car_tank -= cost[index-1]
            # print(Car_tank, index, gas[index], cost[index])
            if Car_tank + gas[index] >= cost[index]:
                Car_tank += gas[index] 
                index += 1
                continue
            else:
                Car_tank = 0
                index += 1
                start_point = index
                Index_is_at_start = True
        if index == len(gas):
            index = 0


        return start_point
