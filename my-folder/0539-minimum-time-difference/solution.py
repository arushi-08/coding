class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        for i in range(len(timePoints)):
            hours, mins = timePoints[i].split(":")
            int_mins = int(hours) * 60 + int(mins)
            timePoints[i] = int_mins
        
        timePoints.sort()
        min_mins = float("inf")
        for t1, t2 in zip(timePoints, timePoints[1:] + timePoints[:1]):
            min_mins = min(min_mins, (t2 - t1)%(24*60))
        
        return min_mins
