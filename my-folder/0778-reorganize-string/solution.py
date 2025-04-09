class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        goal: put most frequent char first such that same chars are not adjacent

        cannot do all k's then repeat vvvlo ['v', 'l', 'o', 'v'], expected vlvov
        cannot do k every consecutive aabbcc, output: ababc_ cannot do it, expected abcabc
        what did i do before?
        put k every consecutive but don't restart the start pointer => abacbc
        abc
        
        """

        s_list = list(s)
        s_map = Counter(s_list)

        heap = [(-v,k) for k, v in s_map.items()]
        heapify(heap)

        res = []
        prev = None
        while heap:
            
            maxval, most_freq_char = heappop(heap)
            res.append(most_freq_char)
            maxval += 1

            if prev:
                heappush(heap, prev)
                prev = None
            
            if maxval < 0:
                prev = (maxval, most_freq_char)

        if len(res) != len(s):
            return ""

        return "".join(res)

# aabbcc
# res = []
# a:2,b:2,c:2
# maxval=-2,most_freq=a
# 
# 


