class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        # iterate on arr
        # keep going ascending then descending and save it

        ascending_count = 0
        descending_count = 0
        mountain_len = 0

        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                left = i - 1
                right = i + 1
                while left >= 0 and arr[left] < arr[left+1]:
                    left -= 1
                while right < len(arr) and arr[right] < arr[right-1]:
                    right += 1
                mountain_len = max(mountain_len, right - left - 1)

        return mountain_len

