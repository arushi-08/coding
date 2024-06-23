class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        k -= 1
        kcounter = 1
        missingval = 1
        i = 0
        while i < len(arr):
            if arr[i] > missingval and k:
                k -= 1
            elif arr[i] == missingval:
                i += 1
            elif not k:
                return missingval
            missingval += 1
        
        while k:
            missingval += 1
            k -= 1

        return missingval





