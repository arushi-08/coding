class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        # derived from bitwise xor of adj values
        # in binary array original;
        # for last idx, derived[i] = original[i] ^ original[0]
        # return true/false
        # 
        # intuition: each elem of original array is getting used twice to form derived array
        # derived array is A[i] ^ A[i+1] and each element is getting called twice
        # so derived array xor has to be 0
        # if it's 0, then derived array is valid, else invalid
        # 
        xor = 0
        for num in derived:
            xor ^= num
        
        return xor & 1 == 0
