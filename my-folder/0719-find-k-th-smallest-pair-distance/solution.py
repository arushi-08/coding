class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        def enough(distance):
            i, j = 0, 0
            count = 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k # count of # pairs is atleast k
        
        st, ed = 0, nums[-1] - nums[0]
        counter = 0
        while st < ed:
            mid = (ed + st)//2
            
            if enough(mid):
                ed = mid
            else:
                st = mid + 1
        return st
        


