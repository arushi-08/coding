class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # iterate on strs
        # store items in hmap, indexed by the tuple(sorted(strs))
        # return hmap.values

        hmap = defaultdict(list)

        for i in range(len(strs)):
            hmap[tuple(sorted(strs[i]))].append(strs[i])
        
        return list(hmap.values())

