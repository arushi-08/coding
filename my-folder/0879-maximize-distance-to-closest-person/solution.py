class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        # 1, 0, 0, 0, 1, 0, 1
        # _, 1, 2, 3, _, 1, _
        # _, 3, 2, 1, _, 1, _

        left_dist = []
        closest_1_idx = float('-inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                left_dist.append(0)
                closest_1_idx = i
            else:
                left_dist.append(i - closest_1_idx)

        closest_1_idx = float('inf')
        right_dist = [0]*len(seats)
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                right_dist.append(0)
                closest_1_idx = i
            else:
                right_dist[i] = closest_1_idx - i
        max_dist = 0
        for i in range(len(seats)):
            max_dist = max(max_dist, min(left_dist[i], right_dist[i]))
        
        return max_dist

