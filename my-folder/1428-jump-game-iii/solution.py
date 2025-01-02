class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        # initially at start
        # when at index i, can jump to i + arr[i] or i - arr[i]
        # check if i can reach any index with value 0

        # 2 options
        if start >= len(arr) or start < 0 or arr[start] < 0:
            return False

        if arr[start] == 0:
            return True
        
        arr[start] *= -1
        
        return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
