class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        sthmap = Counter(stones)
        count = 0
        for i in range(len(jewels)):
            count += sthmap[jewels[i]]
        
        return count
