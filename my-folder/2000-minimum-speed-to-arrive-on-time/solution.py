import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        start = 1
        end = 10**9
        minspeed = end
        while start <= end:
            mid = (start + end)//2
            # print("mid", mid, "start", start, "end", end)
            time = 0
            for i in range(len(dist)-1):
                time += math.ceil(dist[i]/mid)
                if time > hour:
                    break
            last = dist[-1]/mid
            if time + last <= hour:
                time += last
                minspeed = min(minspeed, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return minspeed if minspeed != 10**9 else -1


