class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        temp = arr.copy()
        temp.sort()
        hmap = {}
        i = 1
        for x in temp:
            if x in hmap:
                continue
            hmap[x] = i
            i += 1
        
        for i in range(len(arr)):
            arr[i] = hmap[arr[i]]
        
        return arr
        
