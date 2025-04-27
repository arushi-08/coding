class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        """
        given subarr's find sum = k
        key : curr_sum - earlier_sum == k
        earlier_sum == curr_sum - k
        psum[curr_sum - k] is the count of subarrs whose sum from 0 to subarr length is earlier_sum which means the count of subarrs sum is k
        """

        # psum[i] stores sum : count of nums[0..i] with that sum
        # count is not psum[k]
        # it can include between sum that doesn't include nums[0]
        psum = defaultdict(int)
        psum[0] = 1
        curr_sum = 0
        count = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            count += psum[curr_sum - k]
            psum[curr_sum] += 1

        return count



