class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        if len(nums) < 3:
            return []
        
        # nums.sort()
        # ans = []
        # ans2 = []
        # for k in range(len(nums)-1, -1, -1):
        #     for i in range(len(nums)):
        #         for j in range(len(nums)):
        #             if len(set([i,j,k])) == 3:
        #                 if sorted([nums[i], nums[j], nums[k]]) not in ans2 and nums[i] + nums[j] + nums[k] == 0:
        #                     ans2.append(sorted([nums[i], nums[j], nums[k]]))
        #                     ans.append([nums[i], nums[j], nums[k]])
        # return ans
        
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums)-1
            while j < k:
                sum = nums[j] + nums[k] + nums[i]
                if sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
            
                elif sum < 0:
                    j += 1
                
                else:
                    k -= 1
            
            
        
        return ans
