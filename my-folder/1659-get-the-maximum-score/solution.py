class Solution:
    def maxSum(self, A1: List[int], A2: List[int]) -> int:
        
        i, j = 0, 0
        psum1, psum2 = 0, 0
        maxsum = 0
        while i < len(A1) and j < len(A2):
            if A1[i] > A2[j]:
                psum2 += A2[j]
                j += 1
            elif A1[i] < A2[j]:
                psum1 += A1[i]
                i += 1
            else:
                maxsum += max(psum1, psum2) + A1[i]
                i += 1
                j += 1
                psum1, psum2 = 0, 0
        
        while i < len(A1):
            psum1 += A1[i]
            i += 1
        while j < len(A2):
            psum2 += A2[j]
            j += 1
        
        maxsum += max(psum1, psum2)
        
        return maxsum % 1000000007
            
        
        
