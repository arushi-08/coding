class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 8 hours
        
        k_range = range(1, max(piles)+1)
        sum_bananas = sum(piles)
        start = 1
        end = max(piles)
        while start < end:
            piles2 = piles.copy()
            eaten = 0
            mid = (start + end)//2
            # print("new mid", mid) 
            time = 0
            i = 0
            
            for i in range(len(piles2)):
                
                if piles2[i] > 0:
                    if piles2[i] % mid != 0:
                        time += piles2[i]//mid + 1
                    else:
                        time += piles2[i]//mid

                if time > h:
                    break
                
            if time <= h:
                # print("time", time,)
                end = mid
            else:
                start = mid + 1 # bigger k
                
            
            # print("start", start, "mid", mid, "end", end)
            
        return start
