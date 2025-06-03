class Solution:
    def intToRoman(self, num: int) -> str:
        int_n_roman = [[1,'I'],
        [4,'IV'],
        [5,'V'],
        [9,'IX'],
        [10,'X'],
        [40,'XL'],
        [50,'L'],
        [90,'XC'],
        [100,'C'],
        [400,'CD'],
        [500,'D'],
        [900,'CM'],
        [1000,'M']]

        # start right to left

        # consider the number of 10's 
        place = 0
        res = []

        for val, sym in reversed(int_n_roman):

            if num // val:
                res.append(sym * (num//val))
                num %= val
        
        return ''.join(res)
        
