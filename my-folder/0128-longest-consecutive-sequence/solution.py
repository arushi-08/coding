class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0

        nums.sort()
        max_length = 0
        length = 1
        # [1,2,3]
        i = 0
        print(nums)
        while i < len(nums)-1:
            # print('top i', i)
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
                
            if i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
            i += 1
        return max(max_length, length)
