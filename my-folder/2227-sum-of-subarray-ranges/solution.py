class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # sum of all ranges largest - smallest

        ans = 0  
        for i in range(len(nums)):
            largest = -float('inf')
            largest_idx = 0
            smallest = float('inf')
            smallest_idx = 0
            for j in range(i+1, len(nums)):
                if smallest == float('inf') or smallest_idx == i-1:
                    for k in range(i, j+1):
                        if largest < nums[k]:
                            largest = nums[k]
                            largest_idx = k
                        if smallest > nums[k]:
                            smallest = nums[k]
                            smallest_idx = k
                else:
                    if largest < nums[j]:
                        largest = nums[j]
                        largest_idx = k
                    if smallest > nums[j]:
                        smallest = nums[j]
                        smallest_idx = j

                ans += largest - smallest

        return ans
