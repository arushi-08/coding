class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        # find p pairs such that max difference amongst all pairs in minimized
        # no idx appears more than once amongst the p pairs

        # minmize the max diff
        # 1,1 2,3
        # output = 1
        # generate combinations of pairs?
        if p == 0: return 0

        nums.sort()
        
        st = 0
        ed = nums[-1] - nums[0]

        def can_p_pairs_reach_mid(mid):
            # count how many pairs have diff <= mid
            # if pairs is p return True
            pairs_count = 0
            i = len(nums)-1
            while i >= 1:
                if nums[i] - nums[i-1] <= mid:
                    pairs_count += 1
                    i -= 2
                else:
                    i -= 1
            return pairs_count >= p

        res = ed
        while st <= ed:
            mid = (st + ed) // 2
            if can_p_pairs_reach_mid(mid):
                res = mid
                ed = mid - 1
            else:
                st = mid + 1
        
        return res

        

