class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        candidate1 = tops[0]
        candidate2 = bottoms[0]
        
        candidate_common_list = []
        for candidate in [candidate1, candidate2]:
            candidate_common = True
            for i in range(1, len(tops)):
                if candidate != tops[i] and candidate != bottoms[i]:
                    candidate_common = False
                    break
            if candidate_common:
                candidate_common_list.append(candidate)
        
        if not candidate_common_list:
            return -1
        
        global_swaps = len(tops)
        for candidate in candidate_common_list:
            N = len(tops)
            global_swaps = min([global_swaps, N - tops.count(candidate), N - bottoms.count(candidate)])
        
        return global_swaps
            
        
        
        
