class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        
        if len(word2) > len(word1): return []

        last_idx = [-1] * len(word2)
        j = len(word2)-1
        last_val = 0
        for i in range(len(word1)-1,-1,-1):
            if j >= 0 and word2[j] == word1[i]:
                last_idx[j] = i
                j-=1
        
        # print(last_idx)
        i = 0
        j = 0
        result = []
        one_elemt_diff = False

        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif not one_elemt_diff:
                if (
                    j == len(word2)-1 or 
                    i+1<=last_idx[j+1]
                    ):
                    one_elemt_diff = True
                    result.append(i)
                    j += 1
                
            i += 1
        
        if j == len(word2):
            return result
        
        return []


            
