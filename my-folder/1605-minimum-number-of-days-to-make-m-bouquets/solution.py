class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)
        if n < m*k: return -1

        if n == m*k: return max(bloomDay)

        if k == 1:
            bloomDay.sort()
            return bloomDay[m-1]

        
        # try using binary search
        # the number of days is the search space

        # what is the function to select mid?
        def covered_bouquets(day):
            possible_idx = [0]*n
            for i in range(n):
                if bloomDay[i] <= day:
                    if i-1>=0 and possible_idx[i-1]:
                        possible_idx[i] = possible_idx[i-1] + 1
                    else:
                         possible_idx[i] = 1

            bouquets = 0
            i = 0

            # how many subarrays of 1 of k length are possible from a binary array

            while i < len(possible_idx) - k + 1:
                if possible_idx[i] and possible_idx[i+k-1] - possible_idx[i] + 1== k:
                    bouquets += 1
                    i += k
                else:
                    i += 1
            return bouquets

        st = min(bloomDay)
        ed = max(bloomDay)

        while st < ed:
            mid = (st + ed) // 2

            if covered_bouquets(mid) >= m:
                ed = mid 
            else:
                st = mid + 1
        
        return ed
    
