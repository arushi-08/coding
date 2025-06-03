class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        """
        nums[]

        """
        nums.sort()
        print('nums', nums)

        res = set()
        i = 1
        while i < len(nums)-1:
            j = 0
            if nums[j] > 0:
                break
            
            k = len(nums)-1

            while j < i and i < k:
                if nums[j] > 0:
                    break

                cand = nums[i] + nums[j] + nums[k]
                
                if cand == 0:
                    res.add((nums[j], nums[i], nums[k]))
                    k -= 1
                    j += 1
                
                elif cand > 0:
                    k -= 1

                else:
                    j += 1
            
            i += 1
        
        return list(res)
        


                




