import heapq
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # sliding window
        freq = {}
        start = 0
        end = 0
        ans = 0
        for i in range(len(nums)):
            # print("start", i, freq)
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            # if nums[i] not in freq or freq[nums[i]]<=k:
            #     # end += 1
            #     # print(freq)
            # else:
                # print("here", freq, i)
            if freq[nums[i]] > k:
                ans = max(ans, i - start)
            else:
                ans = max(ans, i - start + 1)
            while freq[nums[i]]>k:
                freq[nums[start]] -= 1
                start += 1

        return ans
