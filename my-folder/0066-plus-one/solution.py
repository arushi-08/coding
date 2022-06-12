class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        digits[n-1] += 1
        carry = digits[n-1] / 10
        digits[n-1] = digits[n-1] % 10
        
        for i in range(n-2, -1, -1):
            
            if carry == 1:
                digits[i] += 1
                carry = digits[i] / 10
                digits[i] = digits[i] % 10
        
        if carry == 1:
            digits.insert(0, 1)
        
        return digits
