class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # n cars given position away from the starting mile 0, travelling to reach target
        # given 2 int array: position, speed
        # both of length n
        # where position[i] is starting mile of ith car
        # and speed[i] is speed of ith car in mph

        # 10 speed 2
        # 8 speed 4
        # time = 1 ( =12/(10+2) ), 12, 12

        # time = 12, speed 0

        # 5 speed 1
        # 3 speed 3
        # time = 1, -> 3+3 = 6
        # time = 1, -> 5+1 = 6

        # find the count of car fleets

        """
        position + speed -> dist in time = 1

        if speed is in ascending order of distance, car fleets -> num of cars

        for cars with speed > than cars[i+1] can form fleets
            position / speed  = time
            12 (target) - curr position /3 (speed) = time
            12 - 3 = dist to cover / speed = 9/3 = 3 time
            12 - 5 = 7 / 1 = 7
        """
        if len(speed) == 1: return 1

        car_metrics = list(zip(position, speed))
        car_metrics.sort(reverse=True)

        fleets = 0
        prev_time = 0

        for pos, spd in car_metrics:

            time_to_target = (target - pos) / spd

            if prev_time < time_to_target:
                fleets += 1
                prev_time = time_to_target
        
        return fleets










        





