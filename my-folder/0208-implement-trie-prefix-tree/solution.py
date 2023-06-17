class Node:
    def __init__(self):
        self.children = {}
        self.endofword = False

from collections import deque
class Trie:
    def __init__(self):
        # initialize object
        self.triemap = Node()

    def insert(self, word: str) -> None:
        curr = self.triemap
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.endofword = True

    def search(self, word: str) -> bool:
        curr = self.triemap
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endofword

    def startsWith(self, prefix: str) -> bool:
        curr = self.triemap
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
