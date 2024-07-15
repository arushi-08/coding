class FindUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, key):

        if self.parent[key] != key:
            self.parent[key] = self.find(self.parent[key])

        return self.parent[key]

    def union(self, x, y):
        # remember union is on the parents
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx != parenty:
            if self.rank[parentx] > self.rank[parenty]:
                self.parent[parenty] = parentx
            elif self.rank[parentx] < self.rank[parenty]:
                self.parent[parentx] = parenty
            else:
                self.parent[parentx] = parenty
                self.rank[parenty] += 1
        
            self.count -= 1

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # find union

        logs.sort(key=lambda x:x[0])
        fu = FindUnion(n)

        for log in logs:
            time, x, y = log
            if fu.find(x) != fu.find(y):
                fu.union(x, y)
            if fu.count == 1:
                return time

        return -1

            # {0:[1],1:[0,5],2:[3],3:[4,2]}
            # 0,1,5 | 2,3,4

