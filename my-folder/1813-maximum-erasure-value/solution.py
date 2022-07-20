from collections import defaultdict
class Solution:
    # def prefixSum(self, nums):
    #     psum_list = []
    #     psum = 0
    #     for i in range(len(nums)):
    #         psum += nums[i]
    #         psum_list.append(psum)
    #     return psum_list
        
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        currsum = 0
        currset = set()
        maxsum = 0
        maxset = set()
        
        l = 0
        
        for i in range(len(nums)):
            
            while nums[i] in currset:
                currset.remove(nums[l])
                currsum -= nums[l]
                l += 1
            if currsum + nums[i] < nums[i]:
                currsum = nums[i]
                currset = [nums[i]]
            else:
                currsum += nums[i]
                currset.add(nums[i])

            if maxsum < currsum:
                maxsum = currsum
                maxset = currset
        
        return maxsum
