class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        
        # why is queue giving correct ans but minheap is giving wrong answer?
        # min heap is only prioritizing cost which is incorrect 
        
        if startPos == homePos: return 0

        cost = 0

        if startPos[0] < homePos[0]:
            for i in range(startPos[0], homePos[0]):
                cost += rowCosts[i+1]
        else:
            for i in range(homePos[0], startPos[0]):
                cost += rowCosts[i]
                
        if startPos[1] < homePos[1]:
            for j in range(startPos[1], homePos[1]):
                cost += colCosts[j+1]

        else:
            for j in range(homePos[1], startPos[1]):
                cost += colCosts[j]

        return cost
