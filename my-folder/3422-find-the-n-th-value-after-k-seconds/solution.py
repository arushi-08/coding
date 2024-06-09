class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        
        arr = [1] * n
        
        while k > 0:
            
            for i in range(1, len(arr)):
                arr[i] += arr[i-1]
            k -= 1
        
        return arr[n-1] % (10**9 + 7)
