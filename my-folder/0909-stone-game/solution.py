class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        i = 0
        j = len(piles) - 1
        alice_turn = True
        astones = 0
        bstones = 0
        while i <= j:
            if piles[i] > piles[j]:
                pickidx = i
                i += 1
            else:
                pickidx = j
                j -= 1
            if alice_turn:
                astones += piles[pickidx]
            else:
                bstones += piles[pickidx]

        return astones > bstones
            
