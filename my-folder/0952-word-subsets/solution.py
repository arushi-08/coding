class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        # string b is subset of string a if every letter in b occurs in a including multiplicity

        # wrr is subset of warrior not world

        # words1 has universal string if for every string b in words2, b is subset of a

        # return arr of universal strings in words1
        # words1_set - unique words
        
        # iterate on words1
        # check if every words1 has all substrings

        # instead of checking each substring in words2 how can we do better?

        # if there's a single substring in words2 that isn't in words1 -> sufficient to move to next words1
        
        # char_counts1 = []
        # for wd in words1:
        #     char_count1 = [0]*26
        #     for ch in wd:
        #         char_count1[ord(ch)-ord('a')] += 1
        #     char_counts1.append(char_count1)

        # char_counts2 = []
        # for wd in words2:
        #     char_count2 = [0]*26
        #     for ch in wd:
        #         char_count2[ord(ch)-ord('a')] += 1
        #     char_counts2.append(char_count2)
        
        wdmap_map = {}
        for word2 in words2:
            wdmap2 = Counter(word2)
            for k in wdmap2:
                wdmap_map[k] = max(wdmap2[k], wdmap_map.get(k,0))

        ans = []
        for idx, word1 in enumerate(words1):
            is_universal = True
            wdmap1 = Counter(word1)
            for k in wdmap_map:
                if wdmap_map[k] > wdmap1.get(k,0):
                    is_universal = False
                    break
            if is_universal:
                ans.append(words1[idx])
        
        return ans


