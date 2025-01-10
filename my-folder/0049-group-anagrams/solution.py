class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #  given a string -> group anagrams together
        # same set of chars

        # sorting hmap time - o(nklogk)
        # space - o(nk)
        # 
        # char count hmap time - o(nk)
        anagram_dict = defaultdict(list)
        for i in range(len(strs)): # o(n)
            char_count = [0]*26
            for j in range(len(strs[i])):
                char_count[ord('a') - ord(strs[i][j])] += 1
            anagram_dict[tuple(char_count)].append(strs[i]) 

        return list(anagram_dict.values())

        # char count - a1b2
