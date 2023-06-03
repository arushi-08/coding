from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = {}
        for i in range(len(strs)):
            # print()
            # print(sorted(Counter(strs[i])))
            key = tuple(sorted([(key, val) for key, val in Counter(strs[i]).items()]))
            if key in hmap:
                hmap[key].append(strs[i])
            else:
                hmap[key] = [strs[i]]
        ans = []
        
        for key, val in hmap.items():
            ans.append(val)
        return ans
