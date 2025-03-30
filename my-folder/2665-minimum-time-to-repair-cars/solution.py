class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        # you are given an integer array
        # ranks
        # rank of ith mechanic
        # a mechanic with a rank r can repair n cars in r*n^2 mins

        # you are also given an integer cars representing the total number of cars waiting in the garage to be repaired

        # [4,2,3,1], cars=10
        # output = 16


        # 4*1, 2*4, 3*1, 
        # binary search
        ranks.sort()
        st = 1
        ed = max(ranks) * cars * cars
        ans = ed
        while st <= ed:
            mid = (st + ed)//2
            if self.can_repair(mid, ranks, cars):
                ans = mid
                ed = mid - 1
            else:
                st = mid + 1
        
        return ans
    
    def can_repair(self, time, ranks, cars):

        # given a mid time, check if cars can be repaired
        # if cars <= len(ranks):
        #     return time >= max(ranks)

        cars_remaining = cars
        for i in range(len(ranks)):
            st = 1
            res = -1
            ed = cars_remaining
            while st <= ed:
                mid = (st + ed) // 2
                if ranks[i] * (mid ** 2) <= time:
                    res = mid
                    st = mid + 1
                else:
                    ed = mid - 1
            
            if res != -1:
                cars_remaining -= res
                if cars_remaining <= 0: return True
            else:
                return False

        return cars_remaining <= 0

