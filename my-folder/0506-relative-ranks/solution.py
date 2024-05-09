class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        # hmap will store goals : index(player) 
        # another hmap store indices
        # {3:2, 4:5, 8:3, 9:4, 10:1}
        # 
        hmap = {}
        for i in range(len(score)):
            hmap[score[i]] = i
        hmap = dict(sorted(hmap.items(), reverse=True))
        ans = [0] * len(score)
        print(list(hmap.keys()), list(hmap.values()))
        for i, val in enumerate(list(hmap.keys())):
            if i == 0:
                ans[hmap[val]] = 'Gold Medal'
            elif i == 1:
                ans[hmap[val]] = 'Silver Medal'
            elif i == 2:
                ans[hmap[val]] = 'Bronze Medal'
            else:
                ans[hmap[val]] = str(i+1)

        return ans
            
