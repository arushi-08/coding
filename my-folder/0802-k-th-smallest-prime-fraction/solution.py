class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        # sorted array - binary search
        # mid = arr

        # maxfraction = from array
        # totalsmallerfractions = # of smaller fractions than mid

        n = len(arr)
        left = 0
        right = 1

        
        while left < right:
            mid = (left + right)/2
            j = 1
            maxfraction = 0
            totalsmallerfractions = 0
            num = 0
            den = 0
            for i in range(n-1):
                while j < n and arr[i]/arr[j] >= mid:
                    j += 1
                totalsmallerfractions += n - j # fractions smaller than mid
                if j == n:
                    break
                if maxfraction < arr[i]/arr[j]:
                    maxfraction = arr[i]/arr[j]
                    num = arr[i]
                    den = arr[j]

            if totalsmallerfractions == k:
                return [num, den]
            
            elif totalsmallerfractions > k:
                right = mid
            
            else:
                left = mid
            
        return []
        
