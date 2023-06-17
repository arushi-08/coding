class Node:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.worddict = Node()

    def addWord(self, word: str) -> None:
        curr = self.worddict
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.endofword = True
        # print(curr.children)

    def search(self, word: str) -> bool:
        curr = self.worddict
        def search_in_node(word, node):
            for i, c in enumerate(word):
                if c != '.' and c not in node.children:
                    return False
                if c == '.':
                    for x in node.children.keys():
                        if search_in_node(word[i+1:], node.children[x]):
                            return True
                    return False
                node = node.children[c]
            return node.endofword
        return search_in_node(word, curr)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
