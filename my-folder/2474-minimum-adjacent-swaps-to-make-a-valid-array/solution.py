class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        smallest = min(nums)
        smallest_idx = nums.index(smallest)

        nums = [smallest] + nums[:smallest_idx] + nums[smallest_idx+1:]
        
        largest = max(nums)
        largest_idx = nums[::-1].index(largest)
        return smallest_idx + largest_idx
