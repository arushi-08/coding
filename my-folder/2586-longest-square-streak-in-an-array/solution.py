class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        # check how many numbers after current number
        #   form squares of previous numbers

        # [4,3,6,16,8,2]
        # [4,16,2]

        # check which numbers are squares of one another
        # add them to a set/list
        nums_set = set(nums)
        max_len = -1

        for num in nums:
            candidate_set = set()
            n = num**2
            while n in nums_set:
                candidate_set.add(num)
                candidate_set.add(n)
                n = n**2
            if candidate_set:
                max_len = max(max_len, len(candidate_set))
        
        return max_len






