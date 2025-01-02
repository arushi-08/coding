class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        # find how many vowel st and ed strings in queries range

        # psum?
        vowels = ('a', 'e', 'i', 'o', 'u')
        psum = [0]
        
        for i in range(len(words)):
            if words[i].startswith(vowels) and words[i].endswith(vowels):
                psum.append(1+psum[-1])
            else:
                psum.append(psum[-1])
        
        # 1,1,2,3,4
        ans = []
        for st, ed in queries:
            ans.append(psum[ed+1]-psum[st])
        
        return ans

