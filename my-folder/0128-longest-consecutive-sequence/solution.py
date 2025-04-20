class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # cons elements can be unordered

        # sort it and see
        if not nums: return 0
        numset = set(nums)
        longest_cons_elems = 1

        for num in numset:
            if num-1 not in numset:
                curr_streak = 1
                nextnum = num + 1
                while nextnum in numset:
                    curr_streak += 1
                    nextnum += 1
                
                longest_cons_elems = max(longest_cons_elems, curr_streak)
                
        
        return longest_cons_elems
