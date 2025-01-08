class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all triplets
        # nums[i], nums[j], nums[k]
       
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            st = i + 1
            ed = len(nums)-1
            
            while st < ed:
                    
                add = nums[i] + nums[st] + nums[ed]

                if add == 0:
                    ans.add((nums[i], nums[st], nums[ed]))
                    st += 1
                    ed -= 1

                elif add < 0:
                    st += 1
                else:
                    ed -= 1
                
        
        return list(ans)


