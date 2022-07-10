from collections import deque
class Solution:
    def __init__(self):
        self.memo = {}
    def fillCups(self, amount: List[int]) -> int:
        
        result = 0
        while set(amount) != {0}:
            amount.sort()
            if amount[1] != 0 and amount[2] != 0:
                amount[2] -= 1 
                amount[1] -= 1
            elif amount[2] != 0:
                amount[2] -= 1
                
            result += 1
        return result
