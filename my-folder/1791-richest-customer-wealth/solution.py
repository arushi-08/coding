class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxwealth = 0
        for i in range(len(accounts)):
            value = sum(accounts[i])
            if value > maxwealth:
                maxwealth = value
        
        return maxwealth
