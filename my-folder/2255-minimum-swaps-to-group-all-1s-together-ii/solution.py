class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        # swaps is the number of zeros in a subgroup of length (count of 1's subarray in array) 
        # [1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0]
                                        # 1
        #  1,0,1,2,3,0,0,0,1,0,0,1,2,3,0,0,1,2,3,0,0,0,0,1,2,0,0,1,2,0,0,1,0,0

        
        ones_count = 0
        n = len(nums)
        for i in range(n):
            if nums[i]:
                ones_count += 1
        
        swaps = n
        st = 0
        ed = ones_count - 1
        zero_count = 0
        for i in range(ed+1):
            if not nums[i]:
                zero_count += 1
        swaps = min(swaps, zero_count)

        while st < n:
            if not nums[st]:
                zero_count -= 1
            st += 1

            if st + ones_count < n:
                ed += 1
            else:
                ed = st + ones_count - n - 1
            if not nums[ed]:
                zero_count += 1

            swaps = min(swaps, zero_count)

        return swaps



