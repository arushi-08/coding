class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        hmap = Counter(word)
        greatest_count = max(hmap.values())
        smallest_count = min(hmap.values())
        freq_map = Counter(hmap.values())
        most_freq_count = max(freq_map.values())
        least_freq_count = min(freq_map.values())

        if len(freq_map) > 2:
            return False

        if len(freq_map) == 1:
            # possible to remove 1 from strings like: ccccc, xxx {1:x} or {x:1}
            k, v = next(iter(freq_map.items()))
            if v == 1 or k == 1:
                return True
            # for other cases where freq of char is > 1 e.g. aazz, bbbccc {(x>1):y} -> False
            if k > 1:
                return False

        item1, item2 = freq_map.items()
        k1, v1 = item1
        k2, v2 = item2

        # possible to remove 1 from more freq char {1:x, 2:1} or in general {y:x, (y+1):1}
        if (k1 == k2 + 1 and v1 == 1) or (k2 == k1 + 1 and v2 == 1):
            return True

        # possible to remove 1 from char that has 1 frequency and is the only single char: 
        # e.g. abbcc, accccc, {1:1, x:y}
        if (k1 > k2 and v2 == 1 and k2 == 1) or (k2 > k1 and v1 == 1 and k1 == 1):
            return True

        return False






# # ddaccb 2 1 2 1 - F - 2:2 1:2 greatest count can be most frequent count ifsmaller element is 1
# # bac.   111 - T  1:3
# # aaazzbbb. 3 2 3 - F. 2:1 3:2
# # aazzbbb. 2 2 3 - T. 2:2 3:1
# # zz.     2 - T       2:1
# # cccd.   3 1 - F     3:1 1:1
# # aazz.   2 2 - F      2:2
# # abcc.   1 1 2 - T.    1:2 2:1
# # abbcc.  1 2 2 - T     1:1. 2:2
# # cbccca. 4 1 1 - F    4:1 1:2
