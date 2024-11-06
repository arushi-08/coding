class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        nums_unsorted = nums.copy()
        nums.sort()

        if nums == nums_unsorted: return True

        # 8 can be swapped by 4
        # 4 can be swapped by 2

        # check if adjacent nums need to be swapped and if bit count allows swapping
        # if yes, keep doing it
        n = len(nums_unsorted)
        swaps = [0]*n
        for i in range(n-1):
            if nums_unsorted[i] > nums_unsorted[i+1]:
                if nums_unsorted[i].bit_count() != nums_unsorted[i+1].bit_count():
                    return False
            swaps[i] = nums_unsorted[i].bit_count()
            swaps[i+1] = nums_unsorted[i+1].bit_count()
        
        i = 0
        while i < n:
            st = i
            ed = i
            while i < n-1 and swaps[i] and swaps[i] == swaps[i+1]:
                i += 1
                ed = i
            nums_unsorted[st:ed+1] = sorted(nums_unsorted[st:ed+1])
            # print('inside', st, ed, nums_unsorted)
            i += 1
        # print(nums_unsorted)
        return nums_unsorted == nums

