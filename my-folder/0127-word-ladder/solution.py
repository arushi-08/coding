class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)
        if endWord not in wordSet: return 0

        if beginWord not in wordSet:
            wordSet.add(beginWord)

        graph = defaultdict(list)
        # [*it, h*t]
        for word in wordSet:
            for i in range(len(word)):
                graph[word[:i]+ '*' + word[i+1:]].append(word)

        queue_begin = deque([beginWord])
        visited_begin = {beginWord:1}
        queue_end = deque([endWord])
        visited_end = {endWord:1}

        while queue_begin and queue_end:
            if len(queue_begin) > len(queue_end):
                queue_begin, queue_end = queue_end, queue_begin
                visited_begin, visited_end = visited_end, visited_begin

            queue_len = len(queue_begin)
            for _ in range(queue_len):
                
                curr = queue_begin.popleft()
            
                for i in range(len(curr)):
                    for neigh in graph[curr[:i]+ '*' + curr[i+1:]]:
                        if neigh in visited_end:
                            return visited_begin[curr] + visited_end[neigh]
                        if neigh not in visited_begin:
                            queue_begin.append(neigh)
                            visited_begin[neigh] = visited_begin[curr] + 1
        
        return 0
