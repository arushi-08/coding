class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        nums = [i for i in nums if i != 0]
        ops = 0
        heapify(nums)
        minelem = 0
    
        while nums:
            ops += 1
            temp = []
            minelem = heappop(nums)
            
            while nums:
                elem = heappop(nums)
                diff = elem - minelem
                if diff > 0:
                    heappush(temp, elem - minelem)
            
            nums = temp
            
        return ops
