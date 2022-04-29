from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        queue = deque()
        max_len = 0
        for i in s:
            if i not in queue:
                queue.append(i)
            else:
                max_len = max(max_len, len(queue))
                while i != queue[0]:
                    del queue[0]
                if len(queue) >= 1 and i == queue[0]:
                    del queue[0]
                    queue.append(i)
        
        print(max_len, len(queue), queue)
        max_len = max(max_len, len(queue))
        return max_len
        
