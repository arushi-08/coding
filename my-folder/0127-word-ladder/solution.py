from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList: return 0
        
        # try drawing a graph
        # hit: hot
        # hot: dot, lot
        # dot: hot, dog, lot
        # dog: cog, dot, log
        # lot: dot, hot
        
        graph = {}
        for word in wordList:
            for i in range(len(beginWord)):
                generic = word[:i] + "*" + word[i+1:]
                graph.setdefault(generic, []).append(word)
        
        queue = deque()
        
        queue.append((beginWord, 1))
        
        visited = set([beginWord])
        
        while queue:
            currword, moves = queue.popleft()
            
            if currword == endWord:
                return moves
            
            for i in range(len(currword)):
                generic = currword[:i] + "*" + currword[i+1:]
                if generic in graph:
                    for word in graph[generic]:
                        if word not in visited:
                            queue.append((word, moves+1))
                            visited.add(word)

        return 0
            
        
                
        
