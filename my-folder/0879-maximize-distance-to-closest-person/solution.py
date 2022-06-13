class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        N = len(seats)
        distance = [0] * N
        
        last_occupied = 0
        for i in range(N):
            if seats[i] == 0:
                if seats[last_occupied] == 1:
                    distance[i] = i - last_occupied
                else:
                    pass
            else:
                last_occupied = i
        # print(distance)
        last_occupied = N-1
        for i in range(N-1, -1 ,-1):
            if seats[i] == 0:
                if seats[last_occupied] == 1:
                    if distance[i] == 0:
                        distance[i] = last_occupied - i
                    else:
                        distance[i] = min(distance[i], last_occupied - i)
                else:
                    pass
            else:
                last_occupied = i
        
        return max(distance)
        
