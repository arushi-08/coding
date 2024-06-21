class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        count_nrange = [0] * (n+1)
        for i in range(n):
            count_nrange[nums[i]] += 1
        
        ans = []
        for i in range(1, len(count_nrange)):
            if not count_nrange[i]:
                ans.append(i)
        
        return ans

