class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # climb 1 or 2 steps
        # start from idx 0 or 1
        # reach top
        self.memo = {}

        return min(self.helper(cost, 0), self.helper(cost, 1))
    
    def helper(self, cost, idx):

        if idx >= len(cost):
            return 0
        
        if idx in self.memo:
            return self.memo[idx]

        self.memo[idx] = min(self.helper(cost, idx+1)+cost[idx], 
        self.helper(cost, idx+2)+cost[idx])
    
        return self.memo[idx]
