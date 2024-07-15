class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        # use prefixor -> solves in n^2
        subarray = []
        ans = 0
        prefixor = [0]
        for k in range(len(arr)):
            prefixor.append(prefixor[-1]^arr[k])

        for i in range(1, len(prefixor)-1):
            for j in range(i+1, len(prefixor)):
                if prefixor[i-1]==prefixor[j]:
                    ans += j-i

        return ans
        
