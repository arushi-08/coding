class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        # place fruit in leftmost basket capacity >= quantity of fruit type
        unplaced = 0
        for fruit in fruits:

            for i, basket in enumerate(baskets):

                if fruit <= basket:
                    baskets[i] = -1
                    fruit = 0
                    break
            if fruit:
                unplaced += 1
        
        return unplaced
                
