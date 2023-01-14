class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # remove all occurrences [3,2,2,3] swap 3 with last element
        last_ptr = len(nums)-1
        
        while last_ptr > 0:
            if nums[last_ptr] == val:
                last_ptr -= 1
            else:
                break
        if last_ptr < 0 : return 0 
        if last_ptr == 0:
            if nums[0] == val:
                return 0 
                
        i = 0
        while i < last_ptr and last_ptr > 0:
            if nums[i] == val:
                k = i
                while k <  last_ptr and last_ptr > 0:
                    nums[k], nums[k+1] = nums[k+1], nums[k]
                    k += 1
                last_ptr -= 1
            
            if nums[i] != val:
                i += 1
        
        return last_ptr + 1
            

