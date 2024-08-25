class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = [-1] * size
        self.count = 0
    
    def isLand(self, x):
        if self.parent[x] >= 0:
            return True
        return False
    
    def addLand(self, x):
        if self.parent[x] >= 0:
            return
        self.parent[x] = x
        self.count += 1
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        elif self.rank[yset] > self.rank[xset]:
            self.parent[xset] = yset
        else:
            self.parent[xset] = yset
            self.rank[yset] += 1
        
        self.count -= 1

    def numberofislands(self):
        return self.count

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        '''
        make curr positions[i] to land
        check if neighbor is also land -> union the islands
        return num of islands after converting each pos in positions[i] to land
        '''
        answer = []
        uf = UnionFind(m*n)

        x = [-1, 0, 1, 0]
        y = [0, 1, 0, -1]
        for p in positions:
            landpos = p[0] * n + p[1]
            uf.addLand(landpos)

            for i in range(4):
                neighborx = p[0] + x[i]
                neighbory = p[1] + y[i]
                neighborpos = neighborx * n + neighbory

                if neighborx >= 0 and neighborx < m and neighbory >= 0 and neighbory < n and uf.isLand(neighborpos):
                    uf.union(landpos, neighborpos)

            answer.append(uf.numberofislands())
        
        return answer
