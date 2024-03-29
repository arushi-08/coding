class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        freq = {}
        start = 0
        max_element = max(nums)
        print(max_element)
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            while freq.get(max_element, 0) == k:
                freq[nums[start]]-=1
                start += 1
            ans += start
        
        return ans

                


