class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        # get all increasing digits
        # get all decreasing digits

        ans = 0
        for i in range(1, len(rating)-1):
            j_lt_i = 0
            j_gt_i = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    j_lt_i += 1
                elif rating[j] > rating[i]:
                    j_gt_i += 1
            
            k_lt_i = 0
            k_gt_i = 0
            for k in range(i+1, len(rating)):
                if rating[k] < rating[i]:
                    k_lt_i += 1
                elif rating[k] > rating[i]:
                    k_gt_i += 1
        
            ans += j_lt_i * k_gt_i
            ans += k_lt_i * j_gt_i

        return ans
            


