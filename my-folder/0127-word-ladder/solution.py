from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord: return 0
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        while len(queue):
            curr, count = queue.popleft()
            for word in wordList:
                if word not in visited:
                    changes = 0
                    for c1, c2, in zip(curr, word):
                        if c1 != c2:
                            changes += 1
                    if changes > 1:
                        continue
                    visited.add(word)
                    if word == endWord:
                        return count + 1
                    queue.append((word, count + 1))
        
        if curr == endWord: return count
        return 0
