class Solution:
    def minimumPushes(self, word: str) -> int:
        
        hmap = defaultdict(str)
        number = 2
        press = 1
        for char in word:
            hmap[char] = press
            number += 1
            if number == 10:
                number = 2
                press += 1
        
        ans = 0
        for char in word:
            ans += hmap[char]
        
        return ans
