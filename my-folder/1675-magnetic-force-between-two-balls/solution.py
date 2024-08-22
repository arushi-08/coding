class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        # sort position

        # TTTTTFFFFF
        # max dist

        # [1,2,10,13,14,25], m = 3
        # distances bet balls
        # 1, 9, 12, 13, 24
        # dist = 1 -> 1, 2, 10
        # dist = 9 -> 1, 10, 25
        # dist = 12 -> 1, 13, 25

        # approach
        # calculate distance bet all pos from start
        #  e.g., 1, 9, 12, 13, 24
        # check if balls can be placed on these distances

        
        position.sort()

        # distances = []
        # mindist = float('inf')
        # for i in range(len(position)-1):
        #     mindist = min(mindist, position[i+1]-position[i])

        # distances = list(range(mindist, position[1]-position[0]))

        # for i in range(2, len(position)):
        #     distances.append(position[i] - position[0])
        # print('distances', distances)   

        # return 0
        start = 0
        end = position[-1]-1
        maxdistance = 0

        while start <= end:
            mid = (start + end)//2
            # print('start', distances[start], 'mid', distances[mid])
            if self.is_distance_possible(mid, position, m):
                maxdistance = max(maxdistance, mid)
                start = mid + 1
            else:
                end = mid - 1
        
        return maxdistance

        # [1,2,3,4,5,1000000000] <- positions
        # 1, 2, 3, 4, 99999999 <- distances

        # [75,77,70,22] <- position, m = 3
        # range(1, 22)
        #
        # m = 3

        # distances[mid] = 3


    def is_distance_possible(self, dist, position, m):
            # [1,2,3,4,7]
             # distances[mid] = 3
            #  m = 1
            
            last_ball_placed = position[0]
            i = 1
            m -= 1
            while m and i < len(position):
                if position[i] - last_ball_placed >= dist:
                    m -= 1
                    last_ball_placed = position[i]
                i += 1
            
            if not m:
                return True
            
            return False




