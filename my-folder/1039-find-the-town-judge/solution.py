class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # return i if no outgoing edge from i

        edges = [0] * (n+1)
        trusts = set()
        for a,b in trust:
            edges[a] -= 1 # remove from guy who's trusting
            edges[b] += 1 # add to guy who's trusting
        
        for i in range(1, n+1):
            if edges[i] == n-1:
                return i
        
        return -1
