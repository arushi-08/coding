class Solution:
    def reorganizeString(self, s: str) -> str:
        
        fmap = Counter(s)
        fmap_items = [[-v,k] for k,v in fmap.items()]
        heapify(fmap_items)
        prev = None
        res = []

        while fmap_items:
            freq, top_chr = heappop(fmap_items)
            freq += 1
            res.append(top_chr)

            if prev:
                heappush(fmap_items, prev)
                prev = None
            
            if freq < 0:
                prev = [freq, top_chr]
        
        if len(res) == len(s):
            return ''.join(res)
        return ''
        
