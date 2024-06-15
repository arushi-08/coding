class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        ordermap = {}
        for i in range(len(order)):
            ordermap[order[i]] = i

        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                
                if j >= len(words[i+1]):
                    return False
                if ordermap[words[i][j]] > ordermap[words[i+1][j]]:
                    return False
                elif ordermap[words[i][j]] < ordermap[words[i+1][j]]:
                    break

        return True
