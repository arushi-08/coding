class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(nums)):
            
            bin_form = bin(nums[i])
            res = nums[i]

            j = len(bin_form)-1
            while j >= 0 and bin_form[j] == '1':
                j -= 1

            ones = len(bin_form) - j - 1
            res = bin_form[:j + 1] + '0' + '1' * (ones-1)
            res = int(res, 2)
            
            if res | (res+1) == nums[i]:
                ans.append(res)
            else:
                ans.append(-1)
        
        return ans


