from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not beginWord or not endWord: return 0
        queue = deque()
        queue.append((1, beginWord))
        visited = {beginWord}
        
        word_comb = defaultdict(list)
        
        for word in wordList:
            for j in range(len(beginWord)):
                generic_word = word[:j]  + "*" + word[j+1:]
                word_comb[generic_word].append(word)
        
        
        while len(queue):
            len_q = len(queue)
            for _ in range(len_q):
                result, curr = queue.popleft()

                for i in range(len(curr)):
                    generic_word = curr[:i] + "*" + curr[i + 1:]

                    if generic_word in word_comb:

                        for wd in word_comb[generic_word]:
                            if not wd in visited:
                                if wd == endWord: return result + 1
                                queue.append((result + 1, wd))
                                visited.add(wd)


        return 0
    
        
        
