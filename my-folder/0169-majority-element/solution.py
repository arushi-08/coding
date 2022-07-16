class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # [3,   2,  3]        [2,2,1,1,1,2,2]
# curr:    3,   2,   3         2,2,2,1,1,1,2
# count:   1,   1,   1         1,2,1,1,2,1,1
        
        memory = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if memory != nums[i]:
                counter -= 1
                if counter == 0:
                    memory = nums[i]
                    counter += 1
            else:
                counter += 1
                
        return memory
