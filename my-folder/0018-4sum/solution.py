class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        n = len(nums)
        nums.sort()
        dup = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                if (nums[i],nums[j]) in dup: continue
                dup.add((nums[i],nums[j]))
                k = j+1
                l = n-1
                # print('inside',i+1, n-2, dup, nums[j])
                subtarget = target - (nums[i] + nums[j])
                while k < l:
                    cursum = nums[k] + nums[l]
                    if cursum == subtarget:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        
                    elif cursum < subtarget:
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                    else:
                        l -= 1
                        while l > k and nums[l] == nums[l+1]:
                            l -= 1
        return ans
