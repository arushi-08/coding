class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            k = k % len(nums)
            
            first_elements = nums[-k:]
            for i in range(len(nums) - 1 -k, -1, -1):
                nums[i + k] = nums[i]
            
            for i in range(k):
                nums[i] = first_elements[i]

        
        
        
        # nums = front_list + num/s[:len(nums) - k]
