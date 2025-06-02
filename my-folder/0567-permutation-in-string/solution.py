class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # given 2 strings s1, s2, return true if s2 contains permutation of s1, 
        # or false otherwise

        # true if s1's permutatino is substring of s2
        """
        s2[ed] in s1set - but this doesn't consider dups
        if yes, check if next len(s1) chars are all in s1set
            or check at what point s2[ed] not in s1set
                move st ahead of this
        if no,
            st = ed + 1
         
        """
        if len(s1) > len(s2): return False

        fmap = [0] * 26
        for i in range(len(s1)):
            fmap[ord(s1[i]) - ord('a')] += 1

        st = 0
        ed = 0
        required = len(s1)

        while ed < len(s2):

            if fmap[ ord(s2[ed]) - ord('a')] == 0:

                while s2[st] != s2[ed]:
                    fmap[ ord(s2[st]) - ord('a')] += 1
                    required += 1

                    st += 1
                st += 1
                
            else:

                fmap[ ord(s2[ed]) - ord('a')] -= 1
                required -= 1

                if required == 0:
                    return True
            
            ed += 1
        
        return False



