class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = n - 1
        write_idx = len(A) - 1
        
        while b >= 0:
            if a >= 0 and A[a] > B[b]:
                A[write_idx] = A[a]
                a -= 1
            else:
                A[write_idx] = B[b]
                b -= 1
            write_idx -= 1
