class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """loop from end of array
           keep a variable : carry
           add carry to each arr[i], if arr[i] > 9: carry = arr[i]%10
           arr[i] = arr[i]//10
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                carry = digits[i] // 10
                digits[i] %= 10
            else:
                carry = 0
        
        if carry:
            digits.insert(0, carry)
        
        return digits
