class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # shortest subarray or is atleast k

        if max(nums) >= k: return 1

        sublen = 0
        start = 0
        end = 0
        ors = 0

        for i in range(2, len(nums)+1):
            for j in range(len(nums)):
                ors = 0
                end = min(j+i, len(nums))
                for l in range(j, end):
                    ors |= nums[l]
                    # print(ors, nums[l], l)
                    if ors >= k:
                        # print('inside',ors, nums[l],l)
                        return i
    
        return -1

