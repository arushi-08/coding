class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        sorted_arr = list(set(arr.copy()))
        sorted_arr.sort()
        
        rank = {}
        for i, element in enumerate(sorted_arr):
            rank[element] = i + 1
        
        return [rank[i] for i in arr]
