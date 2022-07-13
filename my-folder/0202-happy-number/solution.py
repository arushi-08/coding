class Solution:
    def isHappy(self, n: int) -> bool:
        
        memory = set()
        while n != 1:
            n_copy = n
            digits_n = 0
            sum_digits = [pow(int(i),2) for i in str(n_copy)]
            sum_digits = sum(sum_digits)
            if sum_digits in memory:
                return False
            memory.add(sum_digits)
            n = sum_digits
        
        return True
