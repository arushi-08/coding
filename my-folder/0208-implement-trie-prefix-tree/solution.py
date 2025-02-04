class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        trie = self.trie
        for ch in word:
            if ch not in trie:
                trie[ch] = {}
            trie = trie[ch]
        trie['#'] = '#'


    def search(self, word: str) -> bool:
        _, ans = self.search_helper(word)
        return ans

    def search_helper(self, word):
        trie = self.trie
        for ch in word:
            if ch not in trie:
                return False, False
            trie = trie[ch]
        return True, '#' in trie

    def startsWith(self, prefix: str) -> bool:
        ans, _ = self.search_helper(prefix)
        return ans


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
