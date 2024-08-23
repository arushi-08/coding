class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        # think in reverse, instead of finding min prefix, suffix 
        # find max subarray 
        # 6, 11 - 5

        totalsum = sum(nums)
        if totalsum == x: return len(nums)
        maxsum = totalsum - x
        st = 0
        currsum = 0 
        maxlength = 0

        # [5,1,4,2,3], 
        # maxsum = 9
        # currsum = 5, ed = 0
        # currsum = 6, ed = 1
        # currsum = 10, ed = 2
        # currsum > maxsum, st = 1, currsum = 5
        # currsum = 7, ed = 3
        # currsum > maxsum, st = 2, currsum = 6
        # currsum == maxsum, maxlength =
        # currsum = 6, ed = 3
        # ed = 4 
        for ed in range(len(nums)):

            while st < ed and currsum > maxsum:
                currsum -= nums[st]
                st += 1
            
            if currsum == maxsum:
                maxlength = max(maxlength, ed - st)
            
            currsum += nums[ed]

        while st < ed and currsum > maxsum:
                currsum -= nums[st]
                st += 1
                
        if currsum == maxsum:
            maxlength = max(maxlength, ed - st + 1)

        if maxlength == 0:
            return -1
        
        return len(nums) - maxlength
