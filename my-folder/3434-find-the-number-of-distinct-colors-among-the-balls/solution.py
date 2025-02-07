class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # find the number of distinct colors among balls
        # after each query return num of distinct colors
        # ball x color y
        # 0, 1, 2, 3  4
        #c1  c2 c2 c4
        # 1,2,2,3

        # map of colors and balls
        hmap = {}
        color_freq = {}
        color_count = 0
        # hmap[color] -> (ball), changing color will be diff
        # linkedlist
        ans = []
        for ball, color in queries:
            if ball in hmap:
                color_freq[hmap[ball]] -= 1
                if color_freq[hmap[ball]] == 0:
                    del color_freq[hmap[ball]]
            
            hmap[ball] = color
            color_freq[color] = color_freq.get(color, 0) + 1
            ans.append(len(color_freq))
        
        return ans
