class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        
        if digits[0] == 0:
            digits.insert(0, 1)
            
        return digits
        
#         integer = 0
#         place = len(digits) - 1
#         for i in digits:
#             integer += i*pow(10, place)
#             place -= 1
        
#         integer += 1
#         print(integer)
        
#         digits = []
#         while(integer > 0):
#             digits.append(integer%10)
#             integer = int(integer/ 10)
            
#         # print(digits)
#         return [digits[i] for i in range(len(digits)-1, -1, -1)]
