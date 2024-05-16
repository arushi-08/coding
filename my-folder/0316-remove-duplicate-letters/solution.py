from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        hmap = Counter(s)
        added = set()
        stack = []
        for i in range(len(s)):
            while stack and s[i] not in added and stack[-1] >= s[i] and hmap[stack[-1]] > 0:
                element = stack.pop()
                added.remove(element)
            
            if s[i] not in added:
                stack.append(s[i])
                added.add(s[i])
            hmap[s[i]] -= 1

        return ''.join(stack)
        

