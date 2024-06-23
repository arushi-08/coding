class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        currpos = (0,0)
        hmap = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
        visited = set()
        
        for p in path:
            visited.add(currpos)
            currpos = (hmap[p][0] + currpos[0], hmap[p][1] + currpos[1])
            if currpos in visited:
                return True
        
        return False

