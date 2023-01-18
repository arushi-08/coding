class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # total no of subarrays whose sum = k
        # 1, 1, 1 
        # 1, 2 == k counter += 1
        # 1, 2, 3 > k remove left_ptr 3-1 == k counter += 1
        # -1, -1, 1
        # -1, -2, -1
        # Determine # sum−k has occurred already, since it will determine the number of times a subarray with sum k has occurred up to the current index. 
        # Every time we encounter a new sum, we make a new entry or increment sum's value in the hashmap corresponding to that sum.
        # We increment the count by the same amount.
        answer = 0
        j = 0
        hmap = {0:1}
        psum = 0
        while j < len(nums):
            psum += nums[j]
            if psum - k in hmap:
                answer += hmap[psum-k]
            hmap[psum] = hmap.get(psum, 0) + 1
            j += 1

        return answer
