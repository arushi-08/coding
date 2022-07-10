class Solution:
    def __init__(self):
        self.memo = []
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        self.memo = [0] * (len(cost) + 1)
        total_cost = 0
        return self.helper([0] + cost, 0)
    
    def helper(self, cost, idx):
        
        if not cost: return 0
        # print(self.memo[idx], idx)
        if self.memo[idx]: return self.memo[idx]
        
        two_step = self.helper(cost[2:], idx + 2) + cost[0]
        one_step = self.helper(cost[1:], idx + 1) + cost[0]
        self.memo[idx] = min(one_step, two_step)
        # print(cost, idx, one_step, two_step)
        
        return self.memo[idx]
        
        
