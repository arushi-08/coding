class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        net = 0
        hmap = {}
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                net += 1
            else:
                net -= 1
            
            if net == 0:
                maxlen = max(maxlen, i+1)

            if net in hmap:
                maxlen = max(maxlen, i - (hmap[net])) 
            else:
                hmap[net] = i

        return maxlen

