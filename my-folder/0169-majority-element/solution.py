class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #               3 ,2 , 3   2, 2, 1, 1, 1, 2, 2
        # counter       1  1.  1.  1, 2, 1, 1, 2, 1, 1
        # i             3  2   3.  2, 2, 2, 1, 1, 1, 2

        counter = 1
        memory = nums[0]
        for i in range(1, len(nums)):
            if memory == nums[i]:
                counter += 1
            else:
                if counter == 1:
                    memory = nums[i]
                else:
                    counter -= 1
        
        return memory
