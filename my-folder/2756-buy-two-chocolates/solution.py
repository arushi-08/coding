class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()

        cost = money - prices[0] - prices[1]
        if cost >= 0:
            return cost
        
        return money
