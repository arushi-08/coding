class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        # return max operations where you delete 2 elements and all ops have same score
        # first 2, last 2, first and last

        self.memo = {}
        maxops = 0

        return self.helper(nums, 0, 0, len(nums)-1)
    
    def helper(self, nums, sumops, st, ed):
        if st > ed - 1:
            return 0
        
        if (st, ed) in self.memo:
            return self.memo[(st, ed)]

        if not sumops:
            condn1 = self.helper(nums, nums[st]+ nums[st+1], st+2, ed)
            condn2 = self.helper(nums, nums[st]+ nums[ed], st+1, ed-1)
            condn3 = self.helper(nums, nums[ed-1] + nums[ed], st, ed-2)
            self.memo[(st, ed)] = max(
                condn1, condn2, condn3
            ) + 1
            # print(self.memo[(st, ed, sumops)])
            return self.memo[(st, ed)]

        condn1, condn2, condn3 = 0, 0, 0
        if nums[st] + nums[st+1] == sumops:
            condn1 = self.helper(nums, sumops, st+2, ed) + 1
        if st+1 != ed and nums[st] + nums[ed] == sumops:
            condn2 = self.helper(nums, sumops, st+1, ed-1) + 1
        if ed-1 != st and nums[ed] + nums[ed-1] == sumops:
            condn3 = self.helper(nums, sumops, st, ed-2) + 1
        
        self.memo[(st, ed)] = max(condn1, condn2, condn3)
        # print("st", nums[st], "ed", nums[ed])
        return self.memo[(st, ed)]


