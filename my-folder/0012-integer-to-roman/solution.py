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

        result = ''
        for val, sym in reversed(int_n_roman):
            if num // val:
                result += (sym * (num//val))
                num = num % val

        return result
        
