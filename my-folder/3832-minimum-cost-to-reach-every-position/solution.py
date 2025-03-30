class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:

        # check if cost of prev < current, if so use that price

        ans = []
        prevmincost = float('inf')
        for i in range(len(cost)):
            if cost[i] > prevmincost:
                ans.append(prevmincost)
            else:
                ans.append(cost[i])
                prevmincost = min(prevmincost, cost[i])

        return ans
