class Node:
    def __init__(self):
        self.links = [None]*2
    
    def contains_key(self, bit):
        return self.links[bit] is not None

    def get(self, bit):
        return self.links[bit]
    
    def put(self, bit, node):
        self.links[bit] = node
    
    def get_max(self, x):
        return x

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.contains_key(bit):
                node.put(bit, Node())
            node = node.get(bit)
    
    def get_max(self, num):
        node = self.root
        maxnum = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.contains_key(1-bit):
                maxnum = maxnum | (1 << i) # set the bit if trie contains opposite bit at ith index
                node = node.get(1-bit) 
            else:
                node = node.get(bit)
        return maxnum

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''
        use trie 
        convert nums to a trie
        iterate on nums and compare with trie
        '''
        trie = Trie()
        for i in range(len(nums)):
            trie.insert(nums[i])
        
        maxnum = 0
        for i in range(len(nums)):
            maxnum = max(maxnum, trie.get_max(nums[i]))
        
        return maxnum

    
