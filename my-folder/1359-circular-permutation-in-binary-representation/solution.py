class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:


        graycodes = [0] * (1<<n)

        for i in range(1 << n):
            graycodes[i] = i ^ i >> 1
        
        result = []
        for i in range(1 << n):
            result.append(start^graycodes[i])
        
        return result
