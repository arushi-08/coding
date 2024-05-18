class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        

        psum = []
        cursum = 0
        for t in travel:
            cursum += t
            psum.append(cursum)

        gbage_last_pos = {'M': 0, 'P': 0, 'G': 0}
        gbage_count = {'M': 0, 'P': 0, 'G': 0}

        for i in range(len(garbage)):
            for k in range(len(garbage[i])):
                gbage_last_pos[garbage[i][k]] = i
                gbage_count[garbage[i][k]] = gbage_count.get(garbage[i][k], 0) + 1
        
        gbage_types = list(gbage_last_pos.keys())
        ans = 0
        for gbage in gbage_types:
            if gbage_last_pos[gbage] > 0:
                ans += gbage_count[gbage] + psum[gbage_last_pos[gbage]-1]
            else:
                ans += gbage_count[gbage] 
        return ans
