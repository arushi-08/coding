class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        # coords of 4 points in 2d space
        # p1,p2,p3,p4
        # true -> if they construct a square
        # sq: if diag same, and all sides same

        arr = [p1,p2,p3,p4]
        arr.sort()
        p1 = arr[0]
        p2 = arr[1]
        p3 = arr[2]
        p4 = arr[3]

        def dist(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2
        
        p1p2 = dist(p1,p2)
        p2p3 = dist(p2,p3)
        p3p4 = dist(p3,p4)
        p1p4 = dist(p1,p4)
        p1p3 = dist(p1,p3)
        p2p4 = dist(p2,p4)

        if p1p2 == 0 or p2p3 == 0 or p3p4 == 0 or p1p4 == 0 or p1p3 == 0 or p2p4 == 0:
            return False

        # p2,p4
        # p1,p3
        if len(set([p1p2, p2p4, p3p4, p1p3])) == 1:
            return p1p4 == p2p3
    
        # p1 p3
        # p2
        return False



