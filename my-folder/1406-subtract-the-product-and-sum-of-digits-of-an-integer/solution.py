class Solution:
    def productSumDigits(self, n):
        temp_n = n
        prod = 1
        sum_digits = 0
        while temp_n >= 1:
            prod *= temp_n%10
            sum_digits += temp_n%10
            temp_n //= 10
        return prod, sum_digits
        
    def subtractProductAndSum(self, n: int) -> int:
        
        prod, sum_digits = self.productSumDigits(n)
        return prod - sum_digits
