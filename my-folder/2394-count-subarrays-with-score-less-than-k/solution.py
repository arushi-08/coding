class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        st = 0

        ans = 0

        currsum = 0

        for ed in range(len(nums)):
            
            currsum += nums[ed]

            while currsum * (ed-st+1) >= k:
                currsum -= nums[st]
                st += 1
            
            ans += ed - st + 1
        
        return ans

