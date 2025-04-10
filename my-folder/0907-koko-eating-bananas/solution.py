class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # koko loves to eat bananas
        # n piles of bananas
        # ith pile has piles[i]
        # guard will come in h hours
        # koko can eat k bananas each hour
        # if piles[i] < k, koko eats piles[i]
        # koko eats min(piles[i], k) each hour
        # return min k such that she can eat all 
        # FFFTTTTT
        # 1st k when all bananas gone
        # 3,6,7,11
        # if len(piles) >= h
        # then max(piles) is k?
        # if len(piles) < h

        if len(piles) == h:
            return max(piles)

        def can_finish(mid):
            i = len(piles)-1
            n_hours_till_now = 0
            while i >= 0:
                n_hours_curr_pile = math.ceil(piles[i]/mid)
                n_hours_till_now += n_hours_curr_pile
                i -= 1
                
            
            return n_hours_till_now <= h
        
        st = 1
        ed = max(piles)
        res = ed
        while st<=ed:
            mid = (st + ed)//2
            if can_finish(mid):
                res = mid
                ed = mid - 1
            else:
                st = mid + 1

        return res
        

        

                # returns smallest number gte?
        # or is it FFTTT, how to interpret bisect.bisect_left() ?
