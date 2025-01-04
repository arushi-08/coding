class Solution:
    def add_word(self, trie, word):
        for ch in word:
            if ch not in trie:
                trie[ch] = {}
            trie = trie[ch]
        trie['#'] = {}
    
    def get_words(self, trie, prefix):
        if self.k == 0:
            return []
        
        res = []
        if '#' in trie:
            self.k -= 1
            res.append(prefix)

        for i in range(26):
            c = chr(ord('a')+i)
            if c in trie:
                res += self.get_words(trie[c], prefix+c)
        return res

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # bucketing sort + trie
        n = len(words)
        wmap = Counter(words)
        bucket = [{} for _ in range(n)]
        self.k = k

        for word, freq in wmap.items():
            self.add_word(bucket[freq], word)
        
        res = []
        for i in range(n-1,0,-1):
            if self.k == 0:
                return res
            
            res += self.get_words(bucket[i], '')
        
        return res
