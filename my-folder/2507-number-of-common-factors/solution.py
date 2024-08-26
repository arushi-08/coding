class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # get all factors of min element
        # see if they % == 0 for bigger element
        max_element = max(a, b)
        min_element = min(a, b)
        sqrt_min = int(min_element ** 0.5)
        factor = 1
        count = set()

        #  a = 12, b = 6
        # 
        while factor <= sqrt_min:
            quotient_min_element, remainder_min_element = divmod(min_element, factor)
            if remainder_min_element == 0:
                if max_element % factor == 0:
                    count.add(factor)
                    if min_element % (max_element//factor) == 0:
                        count.add(int(max_element//factor))
                if max_element % quotient_min_element == 0:
                    count.add(quotient_min_element)
                

            
            factor += 1
        
        return len(count)
            


