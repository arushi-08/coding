class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        # abc, bca
        # cba -> bca

        # op1: if both words contain same chars -> possible
        # op2: transform possible if chars can be swapped
        # e.g. 'aacabb' - a:3, b:2
        #      'bbcbaa' - b:3, a:2 -> transforming a & b -> possible

        # cabbba: c:1, a:2, b:3
        # abbccc: a:1, b:2, c:3

        # abc | 
        # xyz | xyx wont' work

        # can we just compare freq of chars? - number of uniqe char same 

        if set(word1) != set(word2):
            return False

        word1_hmap = {k:v for k, v in sorted(Counter(word1).items(), key=lambda x:x[1])}
        word2_hmap ={k:v for k, v in sorted(Counter(word2).items(), key=lambda x:x[1])}

        for k1, k2 in zip(word1_hmap, word2_hmap):
            if word1_hmap[k1] != word2_hmap[k2]:
                return False
        
        return True




