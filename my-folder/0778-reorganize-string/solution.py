class Solution:
    def reorganizeString(self, s: str) -> str:
        
        fmap = Counter(s)
        fmap_items = [[-v, k] for k, v in fmap.items()]
        heapify(fmap_items)

        prev = None
        result = []

        while fmap_items:
            
            maxval, topchar = heappop(fmap_items)
            if result and topchar == result[-1]:
                return ""
            result.append(topchar)

            maxval += 1

            if prev:
                heappush(fmap_items, prev)
                prev = None
            
            if maxval < 0:
                prev = [maxval, topchar]
        
        if len(result) == len(s):
            return ''.join(result)
        return ''

