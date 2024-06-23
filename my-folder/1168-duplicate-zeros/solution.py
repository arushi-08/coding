class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)
        i =  n-1
        while i >= 0:
            if i + zeros < n:
                arr[i+zeros] = arr[i]
                # print(i, zeros, i+zeros, arr)
            if arr[i] == 0:
                zeros -= 1
                if i+zeros < n:
                    arr[i+zeros] = 0
            i -= 1


