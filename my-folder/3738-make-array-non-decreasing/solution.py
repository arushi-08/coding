class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:

        # given int array nums
        # 1 op: select subarry and replace it with a single element equal to max value
        # return max possible size of array after performing these ops 
        # such that result is non-dec array

        # [4,2,5,3,5]
        # [4,5,5]
        # ans = 3

        # when arr[i] > arr[i+1]
        # need to make arr[i+1] as arr[i]
        # if we do it immediately, or do it on larger subarr
        # final array size is same? - yeah
        # [4,2,5,3,1,5]
        # [4,5,5]

        res = []

        i = 0
        while i < len(nums):
            if res and res[-1] > nums[i]:
                pass
            else:
                res.append(nums[i])
            i += 1

        return len(res)
            
        
        
