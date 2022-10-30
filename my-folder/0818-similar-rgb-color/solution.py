from ast import literal_eval
class Solution:
    def similarRGB(self, color: str) -> str:
        symbols = []
        symbol_hex_val = []
        possible_chars = [str(i) for i in range(10)]
        possible_chars += [i for i in 'abcdef']
        
        for i in possible_chars:
            symbols.append(i+i)
            symbol_hex_val.append(int(i+i, 16))
        
        result = ['#']
        i = 1
        while i < len(color):
            min_symb = ''
            min_val = float('inf')
            for j, symbol_hex in enumerate(symbol_hex_val):
                if (min_val 
                    > abs(
                        symbol_hex - int(color[i:i+2], 16)
                    )
                   ):
                    min_val = abs(
                        symbol_hex - int(color[i:i+2], 16)
                    )
                    min_symb = symbols[j]
            result.append(min_symb)
            i += 2
            
        return ''.join(result)
