from collections import Counter
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
    #         "Flush": Five cards of the same suit.
    # "Three of a Kind": Three cards of the same rank.
    # "Pair": Two cards of the same rank.
    # "High Card": Any single card.
        
        if len(set(suits)) == 1: return "Flush"
        
        ranks_counts = Counter(ranks)
        
        for value in ranks_counts.values():
            
            if value >= 3:
                return "Three of a Kind"
        
        if 2 in ranks_counts.values(): return "Pair"

        if 1 in ranks_counts.values(): return "High Card"
